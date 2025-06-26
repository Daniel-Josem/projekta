from flask import Flask, render_template, session, redirect, url_for
import sqlite3
from app.login import login_blueprint  # Importación correcta
from app.admin import api_blueprint   # Asegúrate de importar tu blueprint de admin

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

app.register_blueprint(login_blueprint)
app.register_blueprint(api_blueprint)  # Registra las rutas API

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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lider (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      usuario_id INTEGER UNIQUE NOT NULL,
      experiencia TEXT,
      materia TEXT,
      lider TEXT,
      telefono TEXT,
      direccion TEXT,
      FOREIGN KEY(usuario_id) REFERENCES Usuario(id) ON DELETE CASCADE
    );''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      descripcion TEXT,
      fecha_vencimiento DATE,
      prioridad TEXT,
      estado TEXT DEFAULT 'pendiente',
      id_proyecto INTEGER,
      id_usuario_asignado INTEGER,
      ruta_archivo TEXT,
      curso_destino TEXT,
      FOREIGN KEY(id_usuario_asignado) REFERENCES Usuario(id) ON DELETE SET NULL
    );''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mensajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emisor_id INTEGER,
    emisor TEXT,
    receptor_id INTEGER,
    mensaje TEXT,
    tipo TEXT DEFAULT 'texto', 
    sticker TEXT, 
    imagen_url TEXT, 
    audio_url TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notificaciones (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      mensaje TEXT NOT NULL,
      leido INTEGER DEFAULT 0,
      fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
      id_usuario INTEGER,
      FOREIGN KEY(id_usuario) REFERENCES Usuario(id) ON DELETE CASCADE
    );''')

    conn.commit()
    conn.close()

# Ejecutar la función de creación de tablas al iniciar
crear_tabla_usuario()

# Rutas principales
@app.route('/')
def landing():
    return render_template('landingpage.html')

@app.route('/administrador')
def administrador():
    return render_template('admin.html')

@app.route('/lideres')
def lideres():
    return render_template('lider.html')

@app.route('/trabajador')
def trabajador():
    return render_template('trabajador.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(debug=True)
