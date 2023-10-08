from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
import random


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()

    def set_appear(self):
        self.resize(500, 500)
        self.setWindowTitle('Генератор пароля')
        self.show()

    def initUI(self):
        txt = QLabel('Введите длинну пароля от 1 до 12:')
        self.input1 = QLineEdit('...')
        self.button = QPushButton('Отправить')
        self.result1 = QLabel(self.result)
        v_line = QVBoxLayout()
        v_line.addWidget(txt, alignment=Qt.AlignLeft)
        v_line.addWidget(self.input1, alignment=Qt.AlignLeft)
        v_line.addWidget(self.button, alignment=Qt.AlignLeft)
        v_line.addWidget(self.result1, alignment=Qt.AlignLeft)
        self.setLayout(v_line)

    def result(self):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        for i in range(self.input1):
            password = ''
            password += random.choice(chars)
            return password


app = QApplication([])
win = Main()
app.exec_()
