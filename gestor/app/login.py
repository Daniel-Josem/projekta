from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import sqlite3

login_blueprint = Blueprint('login', __name__)

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
        cursor.execute('SELECT * FROM trabajador WHERE nombre_usuario = ? AND contraseña = ?', (nombre_usuario, contrasena))
        trabajador = cursor.fetchone()
        conn.close()

        if trabajador:
            session['usuario'] = nombre_usuario
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
            cursor.execute('INSERT INTO trabajador (nombre_completo, nombre_usuario, documento, correo, contraseña) VALUES (?, ?, ?, ?, ?)',
                           (nombre, nombre_usuario, documento, correo, contrasena))
            conn.commit()
            flash('Usuario creado exitosamente.')
            return redirect(url_for('login.login'))  # Correcto para blueprint
        except sqlite3.IntegrityError:
            flash('El nombre de usuario, documento o correo ya existe.')
        finally:
            conn.close()

    return render_template('crear_usuario.html')
