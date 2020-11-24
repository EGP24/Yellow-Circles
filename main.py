import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from UI import Ui_MainWindow
from random import randint as rnd


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)
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
            qp.setBrush(QColor(rnd(0, 255), rnd(0, 255), rnd(0, 255)))
            size = rnd(10, 100)
            coords_and_size = [rnd(0, 500 - size), rnd(self.pushButton.size().height() + 10, 500 - size)]
            qp.drawEllipse(*coords_and_size, size, size)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())