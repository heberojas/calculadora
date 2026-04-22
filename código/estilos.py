def obtener_estilos():
    return """
        QWidget {
            background-color: #0f172a;
        }

        QLineEdit {
            background-color: #020617;
            color: #38bdf8;
            border: 2px solid #1e293b;
            border-radius: 12px;
            padding: 10px;
        }

        QPushButton {
            background-color: #1e293b;
            color: white;
            border-radius: 10px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #334155;
        }

        QPushButton:pressed {
            background-color: #475569;
        }
    """
