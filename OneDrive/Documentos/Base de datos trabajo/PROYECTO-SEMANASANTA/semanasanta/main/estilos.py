# estilos.py

verde = "#4CAF50"
verde_hover = "#45a049"
blanco = "#FFFFFF"
negro = "#000000"
gris_claro = "#F2F2F2"
gris_medio = "#CCCCCC"

estilo_input = f"""
    QLineEdit {{
        background-color: {blanco};
        color: {negro};
        padding: 14px 24px;
        border: 1px solid {gris_medio};
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
estilo_combo = f"""
    QComboBox {{
        background-color: {blanco};
        color: {negro};
        padding: 14px 24px;
        border: 1px solid {gris_medio};
        border-radius: 10px;
        font-size: 18px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
    QComboBox QAbstractItemView {{
        background-color: {blanco};
        selection-background-color: {gris_claro};
        font-size: 16px;
    }}
"""
