# main.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from login_view import vista_login
from registro_view import vista_registro
from estilos import estilo_boton, gris_claro, negro

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Proyectos")
        self.setGeometry(50, 50, 700, 500)
        self.setStyleSheet(f"background-color: {gris_claro};")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.mostrar_home()

    def limpiar_layout(self):
        while self.layout.count():
            widget = self.layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

    def mostrar_home(self):
        self.limpiar_layout()

        logo = QLabel("🗃️")
        logo.setFont(QFont("SF Pro Text", 111))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo = QLabel("¡Bienvenido a tu gestor de proyectos y tareas!")
        titulo.setFont(QFont("SF Pro Text", 18, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(f"color: {negro};")

        btn_login = QPushButton("Iniciar sesión")
        btn_login.setStyleSheet(estilo_boton)
        btn_login.clicked.connect(lambda: self.mostrar_vista(vista_login))

        btn_registro = QPushButton("Registrarse")
        btn_registro.setStyleSheet(estilo_boton)
        btn_registro.clicked.connect(lambda: self.mostrar_vista(vista_registro))

        self.layout.setSpacing(20)
        self.layout.setContentsMargins(50, 40, 50, 40)
        self.layout.addWidget(logo)
        self.layout.addWidget(titulo)
        self.layout.addWidget(btn_login)
        self.layout.addWidget(btn_registro)

    def mostrar_vista(self, vista_func):
        self.limpiar_layout()
        widget = vista_func(callback_volver=self.mostrar_home)
        self.layout.addWidget(widget)

app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(app.exec())

