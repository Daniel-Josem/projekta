# login_view.py
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from estilos import estilo_input, estilo_boton, gris_claro, negro

def vista_login(callback_volver):
    widget = QWidget()
    widget.setStyleSheet(f"background-color: {gris_claro};")

    logo = QLabel("🗃️")
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setFont(QFont("SF Pro Text", 111))

    titulo = QLabel("Gestor de Proyectos")
    titulo.setFont(QFont("SF Pro Text", 18, QFont.Weight.Bold))
    titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    titulo.setStyleSheet(f"color: {negro};")

    input_usuario = QLineEdit()
    input_usuario.setPlaceholderText("Correo o Usuario")
    input_usuario.setStyleSheet(estilo_input)

    input_contrasena = QLineEdit()
    input_contrasena.setPlaceholderText("Contraseña")
    input_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
    input_contrasena.setStyleSheet(estilo_input)

    btn_ingresar = QPushButton("Ingresar")
    btn_ingresar.setStyleSheet(estilo_boton)

    def verificar_datos():
        usuario = input_usuario.text().strip()
        contrasena = input_contrasena.text().strip()
        
        # Verificación simple (esto se puede extender a una validación real con base de datos)
        if not usuario or not contrasena:
            QMessageBox.warning(widget, "Campos vacíos", "Por favor completa todos los campos.")
        else:
            # Aquí se puede agregar la verificación contra la base de datos
            QMessageBox.information(widget, "Inicio de sesión", f"Bienvenido {usuario}")

    btn_ingresar.clicked.connect(verificar_datos)

    layout = QVBoxLayout()
    layout.setSpacing(20)
    layout.setContentsMargins(50, 40, 50, 40)

    layout.addWidget(logo)
    layout.addWidget(titulo)
    layout.addWidget(input_usuario)
    layout.addWidget(input_contrasena)
    layout.addWidget(btn_ingresar)

    widget.setLayout(layout)
    return widget
