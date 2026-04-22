import sys
from PyQt6.QtWidgets import QApplication
from interfaz import Calculadora

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Calculadora()
    ventana.show()

    sys.exit(app.exec())
