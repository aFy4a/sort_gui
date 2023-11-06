from PyQt6.QtWidgets import QApplication
from .widgets import Window

class Application(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        window = Window(self)
        window.show()
        self.window = window

    def exec(self):
        result = QApplication.exec()
        return result
