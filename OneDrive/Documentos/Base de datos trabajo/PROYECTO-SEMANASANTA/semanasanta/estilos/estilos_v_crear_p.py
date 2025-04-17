# --------- COLORES BASE ---------
verde = "#4CAF50"
verde_hover = "#45a049"
blanco = "#FFFFFF"
negro = "#000000"
gris = "#CCCCCC"  # Único gris unificado

# --------- FUENTE BASE ---------
fuente_base = """
    font-family: 'Segoe UI';
    font-size: 14px;
    font-weight: normal;
"""

# --------- ESTILOS ---------

estilo_input = f"""
    QLineEdit, QDateEdit, QComboBox, QListWidget {{
        {fuente_base}
        padding: 8px 12px;
        border: 1px solid {gris};
        border-radius: 6px;
        background-color: {blanco};
        color: {negro};
    }}
"""

estilo_boton = f"""
    QPushButton {{
        {fuente_base}
        background-color: {verde};
        color: {blanco};
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {verde_hover};
    }}
"""

estilo_boton_compacto = f"""
    QPushButton {{
        {fuente_base}
        background-color: {verde};
        color: {blanco};
        padding: 6px 16px;
        border: none;
        border-radius: 6px;
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {verde_hover};
    }}
"""

estilo_etiquetas = f"""
    QLabel {{
        {fuente_base}
        color: {negro};
        font-weight: bold;
        margin-bottom: 4px;
    }}
"""

estilo_tabla = f"""
    QTableWidget {{
        {fuente_base}
        background-color: {blanco};
        border: 1px solid {gris};
        border-radius: 6px;
        gridline-color: {gris};
    }}
    QHeaderView::section {{
        background-color: {gris};
        font-weight: bold;
        padding: 8px;
        border: none;
    }}
    QTableWidget::item {{
        padding: 6px;
    }}
"""

estilo_fondo_blanco = f"""
    QDialog, QWidget {{
        background-color: {blanco};
    }}
"""
