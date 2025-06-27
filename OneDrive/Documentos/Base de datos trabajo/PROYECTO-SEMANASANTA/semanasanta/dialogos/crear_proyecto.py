from PyQt6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QDateEdit, QPushButton, QHBoxLayout,
    QMessageBox, QListWidget, QListWidgetItem, QComboBox, QTableWidget,
    QTableWidgetItem, QLabel, QVBoxLayout, QGroupBox, QSplitter, QWidget,
    QSizePolicy
)
from PyQt6.QtCore import QDate, Qt

from estilos.estilos_v_crear_p import (
    estilo_input, estilo_boton, estilo_boton_compacto,
    estilo_fondo_blanco, estilo_etiquetas, estilo_tabla
)


class DialogoCrearProyecto(QDialog):
    def __init__(self, tabla_proyectos, parent=None):
        super().__init__(parent)
        self.tabla_proyectos = tabla_proyectos
        self.setWindowTitle("Crear Proyecto")
        self.setStyleSheet(estilo_fondo_blanco)

        self.setMinimumSize(1028, 600)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(50, 25, 50, 25)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Panel Izquierdo - Proyecto
        panel_proyectos_widget = QWidget()
        panel_proyectos_layout = QVBoxLayout(panel_proyectos_widget)

        grupo_proyecto = QGroupBox("Datos del Proyecto")
        grupo_proyecto.setStyleSheet(estilo_etiquetas + " QGroupBox::title { subcontrol-origin: margin; left: 10px; }")
        layout_proyecto = QFormLayout()
        layout_proyecto.setSpacing(12)
        layout_proyecto.setContentsMargins(10, 10, 10, 10)

        label_nombre = QLabel("Nombre del Proyecto:")
        label_nombre.setStyleSheet(estilo_etiquetas)
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Ingrese el nombre del proyecto")
        self.nombre_input.setStyleSheet(estilo_input)
        self.nombre_input.setMinimumHeight(40)

        label_inicio = QLabel("Fecha de Inicio:")
        label_inicio.setStyleSheet(estilo_etiquetas)
        self.fecha_inicio_input = QDateEdit(self)
        self.fecha_inicio_input.setCalendarPopup(True)
        self.fecha_inicio_input.setDate(QDate.currentDate())
        self.fecha_inicio_input.setStyleSheet(estilo_input)
        self.fecha_inicio_input.setMinimumHeight(40)

        label_fin = QLabel("Fecha Límite:")
        label_fin.setStyleSheet(estilo_etiquetas)
        self.fecha_fin_input = QDateEdit(self)
        self.fecha_fin_input.setCalendarPopup(True)
        self.fecha_fin_input.setDate(QDate.currentDate().addDays(1))
        self.fecha_fin_input.setStyleSheet(estilo_input)
        self.fecha_fin_input.setMinimumHeight(40)

        label_usuarios = QLabel("Asignar miembros al proyecto:")
        label_usuarios.setStyleSheet(estilo_etiquetas)
        self.lista_usuarios = QListWidget(self)
        self.lista_usuarios.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.lista_usuarios.setStyleSheet(estilo_input)
        self.lista_usuarios.setMinimumHeight(100)
        self.lista_usuarios.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        usuarios_disponibles = ["Ana", "Luis", "Carlos", "María", "Sofía"]
        for usuario in usuarios_disponibles:
            self.lista_usuarios.addItem(QListWidgetItem(usuario))

        layout_proyecto.addRow(label_nombre, self.nombre_input)
        layout_proyecto.addRow(label_inicio, self.fecha_inicio_input)
        layout_proyecto.addRow(label_fin, self.fecha_fin_input)
        layout_proyecto.addRow(label_usuarios, self.lista_usuarios)

        grupo_proyecto.setLayout(layout_proyecto)
        panel_proyectos_layout.addWidget(grupo_proyecto)

        # Panel Derecho - Tareas
        panel_tareas_widget = QWidget()
        panel_tareas_layout = QVBoxLayout(panel_tareas_widget)

        grupo_tareas = QGroupBox("Tareas del Proyecto")
        grupo_tareas.setStyleSheet(estilo_etiquetas + " QGroupBox::title { subcontrol-origin: margin; left: 10px; }")
        layout_tareas = QVBoxLayout()
        layout_tareas.setSpacing(20)
        layout_tareas.setContentsMargins(10, 10, 10, 10)

        cabecera_layout = QHBoxLayout()
        etiqueta_tareas = QLabel("Gestión de Tareas")
        etiqueta_tareas.setStyleSheet(estilo_etiquetas)
        cabecera_layout.addWidget(etiqueta_tareas)
        cabecera_layout.addStretch()

        self.boton_agregar_tarea = QPushButton("Agregar Tarea")
        self.boton_agregar_tarea.setStyleSheet(estilo_boton_compacto)
        self.boton_agregar_tarea.setMinimumHeight(36)
        self.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        cabecera_layout.addWidget(self.boton_agregar_tarea)

        layout_tareas.addLayout(cabecera_layout)

        campos_layout = QHBoxLayout()

        self.descripcion_tarea_input = QLineEdit(self)
        self.descripcion_tarea_input.setPlaceholderText("Descripción")
        self.descripcion_tarea_input.setStyleSheet(estilo_input)
        self.descripcion_tarea_input.setMinimumHeight(40)
        campos_layout.addWidget(self.descripcion_tarea_input)

        self.fecha_vencimiento_input = QDateEdit(self)
        self.fecha_vencimiento_input.setCalendarPopup(True)
        self.fecha_vencimiento_input.setDate(QDate.currentDate())
        self.fecha_vencimiento_input.setStyleSheet(estilo_input)
        self.fecha_vencimiento_input.setMinimumHeight(40)
        campos_layout.addWidget(self.fecha_vencimiento_input)

        self.prioridad_tarea_input = QComboBox(self)
        self.prioridad_tarea_input.addItems(["Baja", "Media", "Alta"])
        self.prioridad_tarea_input.setStyleSheet(estilo_input)
        self.prioridad_tarea_input.setMinimumHeight(40)
        campos_layout.addWidget(self.prioridad_tarea_input)

        layout_tareas.addLayout(campos_layout)

        self.tabla_tareas = QTableWidget(self)
        self.tabla_tareas.setColumnCount(4)
        self.tabla_tareas.setHorizontalHeaderLabels(["Descripción", "Fecha límite", "Prioridad", "Eliminar"])
        self.tabla_tareas.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_tareas.setStyleSheet(estilo_tabla)
        self.tabla_tareas.setMinimumHeight(180)
        self.tabla_tareas.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla_tareas.setAlternatingRowColors(True)
        self.tabla_tareas.verticalHeader().setVisible(False)
        self.tabla_tareas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout_tareas.addWidget(self.tabla_tareas)
        grupo_tareas.setLayout(layout_tareas)
        panel_tareas_layout.addWidget(grupo_tareas)

        # Añadir ambos paneles al splitter
        splitter.addWidget(panel_proyectos_widget)
        splitter.addWidget(panel_tareas_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        splitter.setSizes([400, 600])

        main_layout.addWidget(splitter)

        # Botones finales centrados
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()

        self.boton_crear = QPushButton("Crear")
        self.boton_crear.setStyleSheet(estilo_boton)
        self.boton_crear.setMinimumHeight(36)
        self.boton_crear.clicked.connect(self.crear_proyecto)
        botones_layout.addWidget(self.boton_crear)

        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_cancelar.setStyleSheet(estilo_boton)
        self.boton_cancelar.setMinimumHeight(36)
        self.boton_cancelar.clicked.connect(self.reject)
        botones_layout.addWidget(self.boton_cancelar)

        botones_layout.addStretch()
        main_layout.addLayout(botones_layout)

        self.tareas = []

    def agregar_tarea(self):
        descripcion = self.descripcion_tarea_input.text()
        fecha_vencimiento = self.fecha_vencimiento_input.date()
        prioridad = self.prioridad_tarea_input.currentText()

        if not descripcion:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una descripción para la tarea.")
            return

        fila = self.tabla_tareas.rowCount()
        self.tabla_tareas.insertRow(fila)
        self.tabla_tareas.setItem(fila, 0, QTableWidgetItem(descripcion))
        self.tabla_tareas.setItem(fila, 1, QTableWidgetItem(fecha_vencimiento.toString("yyyy-MM-dd")))
        self.tabla_tareas.setItem(fila, 2, QTableWidgetItem(prioridad))

        eliminar_btn = QPushButton("Eliminar")
        eliminar_btn.setStyleSheet(estilo_boton_compacto)
        eliminar_btn.setMinimumHeight(28)
        eliminar_btn.clicked.connect(lambda: self.eliminar_tarea(fila))
        self.tabla_tareas.setCellWidget(fila, 3, eliminar_btn)

        self.descripcion_tarea_input.clear()

        tarea = {
            "descripcion": descripcion,
            "fecha_vencimiento": fecha_vencimiento.toString("yyyy-MM-dd"),
            "prioridad": prioridad
        }
        self.tareas.append(tarea)

    def eliminar_tarea(self, fila):
        self.tareas.pop(fila)
        self.tabla_tareas.removeRow(fila)

    def crear_proyecto(self):
        nombre = self.nombre_input.text()
        fecha_inicio = self.fecha_inicio_input.date()
        fecha_limite = self.fecha_fin_input.date()

        if not nombre:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un nombre para el proyecto.")
            return

        if fecha_inicio > fecha_limite:
            QMessageBox.warning(self, "Error", "La fecha de inicio no puede ser posterior a la fecha de finalización.")
            return

        if not self.lista_usuarios.selectedItems():
            QMessageBox.warning(self, "Error", "Debe seleccionar al menos un miembro del equipo.")
            return

        self.accept()

    def get_proyecto(self):
        return {
            "nombre": self.nombre_input.text(),
            "inicio": self.fecha_inicio_input.date().toString("yyyy-MM-dd"),
            "fin": self.fecha_fin_input.date().toString("yyyy-MM-dd"),
            "miembros": [item.text() for item in self.lista_usuarios.selectedItems()],
            "tareas": self.tareas
        }
