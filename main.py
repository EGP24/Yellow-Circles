import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint as rnd


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        if self.do_paint:
            qp.setBrush(QColor(255, 255, 0))
            size = rnd(10, 100)
            coords_and_size = [rnd(0, 500 - size), rnd(self.pushButton.size().height(), 500 - size)]
            qp.drawEllipse(*coords_and_size, size, size)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())