from flask import Flask, render_template, session, redirect, url_for
import sqlite3
from app.login import login_blueprint  # Importación correcta

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'
app.register_blueprint(login_blueprint)

# Crear tabla trabajador si no existe
def crear_tabla_trabajador():
    conn = sqlite3.connect('gestor_de_tareas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trabajador (
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

crear_tabla_trabajador()

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
