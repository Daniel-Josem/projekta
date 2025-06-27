from flask import Blueprint, render_template, session, redirect, url_for
import sqlite3

trabajador_blueprint = Blueprint('trabajador', __name__)

@trabajador_blueprint.route('/trabajador')
def trabajador():
    if 'usuario' not in session:
        return redirect(url_for('login.login'))

    grupo_usuario = session.get('grupo')
    print(f"Grupo del usuario logueado: {grupo_usuario}")

    conn = sqlite3.connect('gestor_de_tareas.db')
    conn.row_factory = sqlite3.Row
    tareas = conn.execute('''
        SELECT * FROM tareas
        WHERE TRIM(LOWER(curso_destino)) = TRIM(LOWER(?))
    ''', (grupo_usuario,)).fetchall()
    conn.close()

    print(f"Tareas encontradas: {tareas}")

    return render_template('trabajador.html', tareas=tareas)


