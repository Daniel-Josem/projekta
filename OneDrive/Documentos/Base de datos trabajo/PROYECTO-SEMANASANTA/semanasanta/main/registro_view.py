# registro_view.py
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from estilos import estilo_input, estilo_boton, estilo_combo, gris_claro, negro


def vista_registro(callback_volver):
    widget = QWidget()
    widget.setStyleSheet(f"background-color: {gris_claro};")

    logo = QLabel("🗃️")
    logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    logo.setFont(QFont("SF Pro Text", 111))

    titulo = QLabel("Registro de Usuario")
    titulo.setFont(QFont("SF Pro Text", 18, QFont.Weight.Bold))
    titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    titulo.setStyleSheet(f"color: {negro};")

    input_nombre = QLineEdit()
    input_nombre.setPlaceholderText("Nombre")
    input_nombre.setStyleSheet(estilo_input)

    input_usuario = QLineEdit()
    input_usuario.setPlaceholderText("Correo o Usuario")
    input_usuario.setStyleSheet(estilo_input)

    input_contrasena = QLineEdit()
    input_contrasena.setPlaceholderText("Contraseña")
    input_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
    input_contrasena.setStyleSheet(estilo_input)

    input_confirmar = QLineEdit()
    input_confirmar.setPlaceholderText("Confirmar contraseña")
    input_confirmar.setEchoMode(QLineEdit.EchoMode.Password)
    input_confirmar.setStyleSheet(estilo_input)

    selector_rol = QComboBox()
    selector_rol.addItems(["Usuario", "Administrador"])
    selector_rol.setStyleSheet(estilo_combo)

    btn_registrar = QPushButton("Registrarse")
    btn_registrar.setStyleSheet(estilo_boton)

    def registrar_usuario():
        if not all([
            input_nombre.text(),
            input_usuario.text(),
            input_contrasena.text(),
            input_confirmar.text()
        ]):
            QMessageBox.warning(widget, "Campos vacíos", "Completa todos los campos.")
        elif input_contrasena.text() != input_confirmar.text():
            QMessageBox.warning(widget, "Error", "Las contraseñas no coinciden.")
        elif "@" not in input_usuario.text():
            QMessageBox.warning(widget, "Error", "Ingresa un correo electrónico válido.")
        else:
            rol = selector_rol.currentText()
            QMessageBox.information(
                widget,
                "Registro exitoso",
                f"Usuario {input_usuario.text()} registrado como {rol}."
            )

    btn_registrar.clicked.connect(registrar_usuario)

    layout = QVBoxLayout()
    layout.setSpacing(10)
    layout.setContentsMargins(20, 10, 20, 10)

    layout.addWidget(logo)
    layout.addWidget(titulo)
    layout.addWidget(input_nombre)
    layout.addWidget(input_usuario)
    layout.addWidget(input_contrasena)
    layout.addWidget(input_confirmar)
    layout.addWidget(selector_rol)
    layout.addWidget(btn_registrar)

    widget.setLayout(layout)
    return widget
