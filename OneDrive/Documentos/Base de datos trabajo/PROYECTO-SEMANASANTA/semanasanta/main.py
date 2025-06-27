from PyQt6.QtWidgets import QApplication
import sys
from menu import MainWindow  # Importa la clase MainWindow desde menu.py

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación PyQt6
    ventana = MainWindow()  # Instancia la ventana principal
    ventana.show()  # Muestra la ventana
    sys.exit(app.exec())  # Ejecuta el ciclo de eventos
