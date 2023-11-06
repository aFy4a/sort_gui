from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton
)
from PyQt6.QtCore import pyqtSignal
from .action import sort

class Button(QPushButton):
    myclicked = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, *kwargs)
        self.clicked.connect(self._active_mycklicked)

    def _active_mycklicked(self):
        self.myclicked.emit(1)

class Window(QWidget):
    def __init__(self, app, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.app = app

        container = QVBoxLayout(self)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Введите несколько чисел")
        container.addWidget(self.edit)

        self.result_button = Button("Считать")
        self.result_button.myclicked.connect(self.active_myclicked)
        container.addWidget(self.result_button)

        self.exit_button = Button("Выйти")
        self.exit_button.myclicked.connect(self.app.quit)
        container.addWidget(self.exit_button)

        self.str = ''

    def active_myclicked(self):
        self.str = self.edit.text()

        if self.str != '':
            try:
                arr = list(map(int, self.str.split(" ")))
                self.str = sort(arr)
                self.edit.setText("")
                self.edit.setPlaceholderText(f"Числа меньше 6: {self.str}")
            except Exception:
                self.edit.setText("")
                self.edit.setPlaceholderText("Введите несколько чисел")
