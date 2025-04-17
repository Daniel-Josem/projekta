from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QDialog, QFormLayout, QLineEdit, QDateEdit, QComboBox,
    QDialogButtonBox, QHeaderView, QFrame, QStackedWidget
)
from PyQt6.QtCore import QDate, Qt
import sys
from dialogos.estilos import estilo_input, estilo_boton, estilo_tabla, estilo_barra_lateral, estilo_etiquetas
from dialogos.crear_proyecto import DialogoCrearProyecto
from dialogos.crear_tarea import CrearTareaDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Proyectos y Tareas")
        self.setGeometry(50, 50, 1024, 600)
        self.layout = QHBoxLayout()

        self.contenido = QStackedWidget()
        self.crear_barra_lateral()

        self.layout.addWidget(self.barra_lateral)
        self.layout.addWidget(self.contenido)
        self.setLayout(self.layout)

        self.mostrar_inicio()

    # Agregar este método
    def abrir_crear_proyecto(self):
        dialogo = DialogoCrearProyecto(self.tabla_proyectos)
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # El proyecto se guarda directamente en el diálogo
            pass

    def crear_barra_lateral(self):
        self.barra_lateral = QFrame(self)
        self.barra_lateral.setFixedWidth(200)
        self.barra_lateral.setStyleSheet(estilo_barra_lateral)

        barra_layout = QVBoxLayout()
        barra_layout.setContentsMargins(10, 20, 10, 20)
        barra_layout.setSpacing(20)

        contenedor_superior = QVBoxLayout()
        contenedor_superior.setSpacing(20)

        btn_inicio = QPushButton("Inicio")
        btn_inicio.clicked.connect(self.mostrar_inicio)
        btn_inicio.setStyleSheet(estilo_boton)
        contenedor_superior.addWidget(btn_inicio)

        btn_ver_proyectos = QPushButton("Ver Proyectos")
        btn_ver_proyectos.clicked.connect(self.mostrar_proyectos)
        btn_ver_proyectos.setStyleSheet(estilo_boton)
        contenedor_superior.addWidget(btn_ver_proyectos)

        btn_ver_tareas = QPushButton("Ver Tareas")
        btn_ver_tareas.clicked.connect(self.mostrar_tareas)
        btn_ver_tareas.setStyleSheet(estilo_boton)
        contenedor_superior.addWidget(btn_ver_tareas)

        btn_notificaciones = QPushButton("Notificaciones")
        btn_notificaciones.setStyleSheet(estilo_boton)
        contenedor_superior.addWidget(btn_notificaciones)

        barra_layout.addLayout(contenedor_superior)
        barra_layout.addStretch()

        btn_salir = QPushButton("Salir")
        btn_salir.clicked.connect(self.close)
        btn_salir.setStyleSheet(estilo_boton)
        barra_layout.addWidget(btn_salir)

        self.barra_lateral.setLayout(barra_layout)

    def mostrar_inicio(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 25, 50, 25)
        layout.setSpacing(20)

        etiqueta = QLabel("Bienvenido al Sistema de Gestión de Proyectos")
        etiqueta.setStyleSheet(estilo_etiquetas)
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(etiqueta)
        widget.setLayout(layout)
        self.contenido.addWidget(widget)
        self.contenido.setCurrentWidget(widget)

    def mostrar_proyectos(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        header = QHBoxLayout()
        header.setSpacing(20)
        etiqueta = QLabel("Proyectos")
        etiqueta.setStyleSheet(estilo_etiquetas)
        header.addWidget(etiqueta)
        header.addStretch()

        btn_crear = QPushButton("Crear proyecto")
        btn_crear.setStyleSheet(estilo_boton)
        btn_crear.clicked.connect(self.abrir_crear_proyecto)  # Asegúrate de que esta línea esté conectada a abrir_crear_proyecto
        header.addWidget(btn_crear)
        layout.addLayout(header)

        self.tabla_proyectos = QTableWidget(0, 6)
        self.tabla_proyectos.setHorizontalHeaderLabels([
            "Nombre", "Inicio", "Finalización", "Estado", "Miembros", "Progreso"
        ])
        self.tabla_proyectos.setStyleSheet(estilo_tabla)
        self.tabla_proyectos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.tabla_proyectos)

        widget.setLayout(layout)
        self.contenido.addWidget(widget)
        self.contenido.setCurrentWidget(widget)

    def mostrar_tareas(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        header = QHBoxLayout()
        header.setSpacing(20)
        etiqueta = QLabel("Tareas")
        etiqueta.setStyleSheet(estilo_etiquetas)
        header.addWidget(etiqueta)
        header.addStretch()

        btn_crear = QPushButton("Crear tarea")
        btn_crear.setStyleSheet(estilo_boton)
        btn_crear.clicked.connect(self.abrir_crear_tarea)
        header.addWidget(btn_crear)
        layout.addLayout(header)

        self.tabla_tareas = QTableWidget(0, 5)
        self.tabla_tareas.setHorizontalHeaderLabels([
            "Tarea", "Vencimiento", "Estado", "Prioridad", "Miembro"
        ])
        self.tabla_tareas.setStyleSheet(estilo_tabla)
        self.tabla_tareas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.tabla_tareas)

        widget.setLayout(layout)
        self.contenido.addWidget(widget)
        self.contenido.setCurrentWidget(widget)

    def abrir_crear_tarea(self):
        dialogo = CrearTareaDialog()  # Utiliza el diálogo importado desde el archivo de diálogos
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            tarea = dialogo.get_tarea()
            self.agregar_tarea_a_tabla(tarea)

    def agregar_tarea_a_tabla(self, tarea):
        fila = self.tabla_tareas.rowCount()
        self.tabla_tareas.insertRow(fila)
        self.tabla_tareas.setItem(fila, 0, QTableWidgetItem(tarea["nombre"]))
        self.tabla_tareas.setItem(fila, 1, QTableWidgetItem(tarea["Vencimiento"]))
        self.tabla_tareas.setItem(fila, 2, QTableWidgetItem(tarea["estado"]))
        self.tabla_tareas.setItem(fila, 3, QTableWidgetItem(tarea["prioridad"]))
        self.tabla_tareas.setItem(fila, 4, QTableWidgetItem(tarea["miembro"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
