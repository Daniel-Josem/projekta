# estilos.py

verde = "#4CAF50"
verde_hover = "#45a049"
blanco = "#FFFFFF"
negro = "#000000"
gris = "#CCCCCC"  # Unificado

estilo_input = f"""
    QLineEdit {{
        background-color: {blanco};
        color: {negro};
        padding: 14px 24px;
        border: 1px solid {gris};
        border-radius: 10px;
        font-size: 18px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
"""

estilo_boton = f"""
    QPushButton {{
        background-color: {verde};
        color: {blanco};
        padding: 14px 24px;
        border: none;
        border-radius: 10px;
        font-size: 18px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {verde_hover};
    }}
"""

estilo_tabla = f"""
    QTableWidget {{
        background-color: {blanco};
        border: 1px solid {gris};
        border-radius: 10px;
        font-size: 16px;
    }}
    QHeaderView::section {{
        background-color: {gris};
        font-weight: bold;
        padding: 10px;
        border: none;
    }}
    QTableWidget::item {{
        padding: 10px;
    }}
"""

estilo_barra_lateral = f"""
    QFrame {{
        background-color: {blanco};
        border-right: 1px solid {gris};
    }}
"""

estilo_etiquetas = f"""
    QLabel {{
        color: {negro};
        font-size: 22px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
"""
