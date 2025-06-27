# Colores base
verde = "#4CAF50"         # Verde principal
verde_hover = "#45a049"   # Verde al pasar el cursor
blanco = "#FFFFFF"        # Blanco
negro = "#000000"         # Negro
gris = "#CCCCCC"          # Gris unificado

# --------- ESTILOS MODERNOS ---------

estilo_input = f"""
    QLineEdit {{
        background-color: {blanco};        # Blanco
        color: {negro};                    # Negro
        padding: 14px 24px;
        border: 1px solid {gris};          # Gris
        border-radius: 10px;
        font-size: 18px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
"""

estilo_boton = f"""
    QPushButton {{
        background-color: {verde};         # Verde
        color: {blanco};                   # Blanco
        padding: 14px 24px;
        border: none;
        border-radius: 10px;
        font-size: 18px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {verde_hover};   # Verde hover
    }}
"""

estilo_tabla = f"""
    QTableWidget {{
        background-color: {blanco};        # Blanco
        border: 1px solid {gris};          # Gris
        border-radius: 10px;
        font-size: 16px;
    }}
    QHeaderView::section {{
        background-color: {gris};          # Gris
        font-weight: bold;
        padding: 10px;
        border: none;
    }}
    QTableWidget::item {{
        padding: 10px;
    }}
"""

estilo_etiquetas = f"""
    QLabel {{
        color: {negro};                    # Negro
        font-size: 18px;
        font-family: 'SF Pro Text';
        font-weight: bold;
    }}
"""

estilo_fondo_blanco = f"""
    QDialog, QWidget {{
        background-color: {blanco};        # Blanco
    }}
"""

# --------- ESTILOS MÁS SIMPLES ---------

estilo_etiquetas = """
    QLabel {
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 5px;
        color: #000000;                    # Negro explícito
    }
"""

estilo_input = """
    QLineEdit, QDateEdit, QComboBox, QListWidget {
        padding: 6px;
        border: 1px solid #ccc;            # Gris claro
        border-radius: 6px;
        font-size: 14px;
    }
"""

# Botón compacto, verde, letra blanca
estilo_boton_compacto = f"""
    QPushButton {{
        background-color: {verde};         # Verde
        color: {blanco};                   # Blanco
        font-weight: bold;
        padding: 6px 16px;
        border: none;
        border-radius: 6px;
        font-size: 14px;
    }}
    QPushButton:hover {{
        background-color: {verde_hover};   # Verde hover
    }}
"""

estilo_fondo_blanco = """
    QDialog {
        background-color: white;           # Blanco
    }
"""

estilo_tabla = """
    QTableWidget {
        border: 1px solid #ccc;            # Gris claro
        border-radius: 6px;
        font-size: 13px;
    }
    QHeaderView::section {
        background-color: #f0f0f0;         # Gris muy claro
        font-weight: bold;
        padding: 4px;
        border: none;
    }
"""

# --------- CON FUENTE BASE ---------

fuente_base = """
    font-family: 'Segoe UI';
    font-weight: normal;
    font-size: 14px;
"""

estilo_fondo_blanco = """
    background-color: white;               # Blanco
"""

estilo_input = f"""
    {fuente_base}
    padding: 6px;
    border: 1px solid #ccc;                # Gris claro
    border-radius: 5px;
"""

# Botón compacto con fuente base y colores verde + blanco
estilo_boton = f"""
    {fuente_base}
    background-color: {verde};             # Verde
    color: {blanco};                       # Blanco
    padding: 6px 12px;
    border: none;
    border-radius: 5px;
"""

estilo_etiquetas = f"""
    {fuente_base}
    color: #333;                           # Gris oscuro
"""

estilo_tabla = f"""
    {fuente_base}
    border: 1px solid #ddd;                # Gris claro
    gridline-color: #ccc;
"""
