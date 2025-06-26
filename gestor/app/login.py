from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import sqlite3

login_blueprint = Blueprint('login', __name__)

# Crear tabla Usuario si no existe
def crear_tabla_usuario():
    conn = sqlite3.connect('gestor_de_tareas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo TEXT NOT NULL,
            nombre_usuario TEXT NOT NULL UNIQUE,
            documento TEXT NOT NULL UNIQUE,
            correo TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL,
            rol TEXT DEFAULT 'trabajador',
            estado TEXT DEFAULT 'activo'
        )
    ''')

    conn.commit()
    conn.close()

# Crear usuarios iniciales (admin y lider)
def crear_usuarios_iniciales():
    usuarios = [
        {
            'nombre_completo': 'Admin Principal',
            'nombre_usuario': 'admin',
            'documento': '1001',
            'correo': 'admin@correo.com',
            'contraseña': 'admin123',
            'rol': 'admin'
        },
        {
            'nombre_completo': 'Líder Operativo',
            'nombre_usuario': 'lider',
            'documento': '1002',
            'correo': 'lider@correo.com',
            'contraseña': 'lider123',
            'rol': 'lider'
        }
    ]

    conn = sqlite3.connect('gestor_de_tareas.db')
    cursor = conn.cursor()

    for usuario in usuarios:
        cursor.execute("SELECT * FROM Usuario WHERE nombre_usuario = ?", (usuario['nombre_usuario'],))
        existente = cursor.fetchone()
        if not existente:
            cursor.execute('''
                INSERT INTO Usuario (nombre_completo, nombre_usuario, documento, correo, contraseña, rol)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                usuario['nombre_completo'],
                usuario['nombre_usuario'],
                usuario['documento'],
                usuario['correo'],
                usuario['contraseña'],
                usuario['rol']
            ))

    conn.commit()
    conn.close()

# Ejecutar al importar el blueprint
crear_tabla_usuario()
crear_usuarios_iniciales()

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('gestor_de_tareas.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta del login
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE nombre_usuario = ? AND contraseña = ?', (nombre_usuario, contrasena))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            session['usuario'] = nombre_usuario
            rol = usuario['rol']

            if rol == 'admin':
                return redirect(url_for('administrador'))
            elif rol == 'lider':
                return redirect(url_for('lideres'))
            else:
                return redirect(url_for('trabajador'))
        else:
            flash('Usuario o contraseña incorrectos.')

    return render_template('login.html')

# Ruta del registro
@login_blueprint.route('/crear_usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombre_usuario = request.form['nombre_usuario']
        documento = request.form['documento']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO Usuario (nombre_completo, nombre_usuario, documento, correo, contraseña) VALUES (?, ?, ?, ?, ?)',
                           (nombre, nombre_usuario, documento, correo, contrasena))
            conn.commit()
            flash('Usuario creado exitosamente.')
            return redirect(url_for('login.login'))  # Correcto para blueprint
        except sqlite3.IntegrityError:
            flash('El nombre de usuario, documento o correo ya existe.')
        finally:
            conn.close()

    return render_template('crear_usuario.html')
