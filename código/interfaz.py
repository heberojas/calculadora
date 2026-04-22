from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from logica import evaluar, traducir_input
from estilos import obtener_estilos


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Pro")
        self.resize(380, 460)

        self.layout = QGridLayout(self)

        self.display = QLineEdit()
        self.display.setFont(QFont("Segoe UI", 20))
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(60)

        self.layout.addWidget(self.display, 0, 0, 1, 5)

        self.crear_botones()
        self.setStyleSheet(obtener_estilos())

    def crear_botones(self):
        botones = [
            ['7', '8', '9', '/', '√'],
            ['4', '5', '6', '*', '^'],
            ['1', '2', '3', '-', 'log'],
            ['0', '.', '=', '+', 'sin'],
            ['C', '(', ')', 'cos', 'tan']
        ]

        for i, fila in enumerate(botones, start=1):
            for j, texto in enumerate(fila):
                btn = QPushButton(texto)
                btn.setFont(QFont("Segoe UI", 11))
                btn.setFixedHeight(50)

                btn.clicked.connect(lambda _, t=texto: self.click(t))
                self.layout.addWidget(btn, i, j)

    def click(self, valor):
        if valor == "=":
            self.display.setText(evaluar(self.display.text()))
        elif valor == "C":
            self.display.clear()
        else:
            nuevo = traducir_input(self.display.text(), valor)
            self.display.setText(nuevo)

    def keyPressEvent(self, event):
        t = event.text()

        if t in "0123456789+-*/().":
            self.display.setText(self.display.text() + t)
        elif event.key() == Qt.Key.Key_Return:
            self.display.setText(evaluar(self.display.text()))
        elif event.key() == Qt.Key.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
