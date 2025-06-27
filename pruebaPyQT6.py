import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QLineEdit
)
from PyQt6.QtCore import Qt

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Gestión de Proyectos")
ventana.setGeometry(200, 100, 1280, 720)

# Diseño principal vertical
layout_principal = QVBoxLayout()
layout_principal.setSpacing(15)
layout_principal.setContentsMargins(20, 20, 20, 20)  # izquierda, arriba, derecha, abajo

# ==== MENÚ DE USUARIO ====
barra_usuario = QHBoxLayout()

# Emoji + nombre del usuario
nombre_usuario = QLabel("Hola, Usuario")
nombre_usuario.setStyleSheet("font-size: 30px; font-weight: bold;")
barra_usuario.addWidget(nombre_usuario)

# Espaciador
barra_usuario.addStretch()

# Botón de notificaciones
notificaciones = QPushButton("🔔")
notificaciones.setStyleSheet("""
    QPushButton {
        background-color: #5ab92d;
        color: white;
        padding: 12px 24px;
        border-radius: 18px;
        font-size: 20px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #007100;
    }
""")
barra_usuario.addWidget(notificaciones)

# Botones Mi perfil y Cerrar sesión
boton_perfil = QPushButton("Mi Perfil")
boton_cerrar = QPushButton("Salir")
boton_perfil.setCursor(Qt.CursorShape.PointingHandCursor)
boton_cerrar.setCursor(Qt.CursorShape.PointingHandCursor)

# Estilo de botones
estilo_boton_usuario = """
    QPushButton {
        background-color: #5ab92d;
        color: white;
        padding: 12px 24px;
        border-radius: 18px;
        font-size: 20px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #007100;
    }
""" 
boton_perfil.setStyleSheet(estilo_boton_usuario)
boton_cerrar.setStyleSheet(estilo_boton_usuario)

barra_usuario.addWidget(boton_perfil)
barra_usuario.addWidget(boton_cerrar)

# Agregar la barra al layout principal
layout_principal.addLayout(barra_usuario)

# Botón para crear un nuevo proyecto
boton_crear = QPushButton("Crear")
boton_crear.setStyleSheet("""
    QPushButton {
        background-color: #5ab92d;
        color: white;
        padding: 12px 26px;
        border-radius: 18px;
        font-size: 26px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #007100;
    }
""")
botones_layout = QHBoxLayout()
botones_layout.addWidget(boton_crear)
botones_layout.addStretch()
layout_principal.addLayout(botones_layout)

# Etiqueta y tabla de proyectos
etiqueta_proyecto = QLabel("Proyectos")
etiqueta_proyecto.setAlignment(Qt.AlignmentFlag.AlignLeft)
etiqueta_proyecto.setStyleSheet("""font-size: 26px;
                                font-family: 'Segoe UI';
                                font-weight: bold;""")
layout_principal.addWidget(etiqueta_proyecto)

tabla = QTableWidget()
tabla.setColumnCount(7)
tabla.setHorizontalHeaderLabels([
    "Proyectos", "Participantes", "Estado", "Fecha Inicio",
    "Fecha Entrega", "Progreso", "Prioridad"
])
layout_principal.addWidget(tabla)

# Etiqueta y tabla de tareas
etiqueta_tarea = QLabel("Tareas")
etiqueta_tarea.setAlignment(Qt.AlignmentFlag.AlignLeft)
etiqueta_tarea.setStyleSheet("""font-size: 26px;
                                font-family: 'Segoe UI';
                                font-weight: bold;""")
layout_principal.addWidget(etiqueta_tarea)

tabla_tareas = QTableWidget()
tabla_tareas.setColumnCount(6)
tabla_tareas.setHorizontalHeaderLabels([
    "Tareas", "Miembros", "Fecha Inicio", "Fecha Final",
    "Estado", "Prioridad"
])
layout_principal.addWidget(tabla_tareas)

# Establecer el diseño y mostrar la ventana
ventana.setLayout(layout_principal)
ventana.show()
sys.exit(app.exec())
