import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from model import Calculator 


class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.calculator = Calculator()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.input = QLineEdit(self)
        self.input.setReadOnly(True)
        layout.addWidget(self.input)

        grid_layout = QGridLayout()
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), 'C': (3, 1), '=': (3, 2), '+': (3, 3)
        }

        self.buttons = {}
        for text, pos in buttons.items():
            self.buttons[text] = QPushButton(text, self)
            self.buttons[text].clicked.connect(lambda checked, t=text: self.on_button_click(t))
            grid_layout.addWidget(self.buttons[text], pos[0], pos[1])

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self, char):
        if char == "C":
            self.calculator.clear_expression()
            self.input.setText("")
        elif char == "=":
            result = self.calculator.calculate()
            self.input.setText(str(result))
        else:
            self.calculator.add_to_expression(char)
            self.input.setText(self.calculator.get_expression())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
