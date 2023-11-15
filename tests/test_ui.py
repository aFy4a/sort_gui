from pytestqt.qt_compat import qt_api
from sort_gui.gui.application import Application, Window


def test_first(qtbot):
    window = Window()
    qtbot.addWidget(window)

    window.edit.setText('1 2 3')
    qtbot.mouseClick(window.result_button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert window.str == '1 2 3 '

def test_second(qtbot):
    window = Window()
    qtbot.addWidget(window)

    window.edit.setText('1 2 3 56')
    qtbot.mouseClick(window.result_button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert window.str == '1 2 3 '

def test_third(qtbot):
    window = Window()
    qtbot.addWidget(window)

    window.edit.setText('')
    qtbot.mouseClick(window.result_button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert window.str == ''