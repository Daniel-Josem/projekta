from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit, QComboBox,
    QDialogButtonBox, QLabel, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import QDate, Qt

from estilos.estilos_v_crear_p import (
    estilo_input, estilo_boton, estilo_etiquetas, estilo_fondo_blanco
)

class CrearTareaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear nueva tarea")
        self.setMinimumSize(400, 400)
        self.setStyleSheet(estilo_fondo_blanco)

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        form_layout = QFormLayout()
        form_layout.setSpacing(12)

        # Nombre
        label_nombre = QLabel("Nombre de la tarea:")
        label_nombre.setStyleSheet(estilo_etiquetas)
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Ingrese el nombre de la tarea")
        self.nombre_input.setStyleSheet(estilo_input)
        self.nombre_input.setMinimumHeight(36)
        form_layout.addRow(label_nombre, self.nombre_input)

        # Fecha vencimiento
        label_fecha = QLabel("Fecha de vencimiento:")
        label_fecha.setStyleSheet(estilo_etiquetas)
        self.fecha_vencimiento_input = QDateEdit(QDate.currentDate())
        self.fecha_vencimiento_input.setCalendarPopup(True)
        self.fecha_vencimiento_input.setStyleSheet(estilo_input)
        self.fecha_vencimiento_input.setMinimumHeight(36)
        form_layout.addRow(label_fecha, self.fecha_vencimiento_input)

        # Estado
        label_estado = QLabel("Estado:")
        label_estado.setStyleSheet(estilo_etiquetas)
        self.estado_input = QComboBox()
        self.estado_input.addItems(["Pendiente", "En progreso", "Completada"])
        self.estado_input.setStyleSheet(estilo_input)
        self.estado_input.setMinimumHeight(36)
        form_layout.addRow(label_estado, self.estado_input)

        # Prioridad
        label_prioridad = QLabel("Prioridad:")
        label_prioridad.setStyleSheet(estilo_etiquetas)
        self.prioridad_input = QComboBox()
        self.prioridad_input.addItems(["Baja", "Media", "Alta"])
        self.prioridad_input.setStyleSheet(estilo_input)
        self.prioridad_input.setMinimumHeight(36)
        form_layout.addRow(label_prioridad, self.prioridad_input)

        # Miembros asignados (selección múltiple)
        label_miembro = QLabel("Miembros asignados:")
        label_miembro.setStyleSheet(estilo_etiquetas)
        self.miembro_input = QListWidget()
        self.miembro_input.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        miembros_ejemplo = ["Juan Pérez", "María López", "Carlos Rodríguez", "Ana Torres", "Luis Fernández"]
        for miembro in miembros_ejemplo:
            item = QListWidgetItem(miembro)
            self.miembro_input.addItem(item)
        self.miembro_input.setStyleSheet(estilo_input)
        self.miembro_input.setMinimumHeight(100)
        form_layout.addRow(label_miembro, self.miembro_input)

        layout.addLayout(form_layout)

        # Botones
        self.boton_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.boton_box.button(QDialogButtonBox.StandardButton.Ok).setStyleSheet(estilo_boton)
        self.boton_box.button(QDialogButtonBox.StandardButton.Cancel).setStyleSheet(estilo_boton)
        self.boton_box.button(QDialogButtonBox.StandardButton.Ok).setMinimumHeight(36)
        self.boton_box.button(QDialogButtonBox.StandardButton.Cancel).setMinimumHeight(36)
        self.boton_box.accepted.connect(self.accept)
        self.boton_box.rejected.connect(self.reject)
        layout.addWidget(self.boton_box)

        self.setLayout(layout)

    def get_tarea(self):
        miembros_seleccionados = [
            item.text() for item in self.miembro_input.selectedItems()
        ]
        return {
            "nombre": self.nombre_input.text(),
            "vencimiento": self.fecha_vencimiento_input.date().toString("yyyy-MM-dd"),
            "estado": self.estado_input.currentText(),
            "prioridad": self.prioridad_input.currentText(),
            "miembros": miembros_seleccionados
        }
