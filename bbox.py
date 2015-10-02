import random, sys
from PyQt4.QtCore import QPoint, QRect, QSize, Qt
from PyQt4.QtGui import *



class Window(QMainWindow):

    def __init__(self, parent=None):

        super(Window, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()
        self.repaint()
    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.origin = QPoint(event.pos())
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()

    def mouseMoveEvent(self, event):

        if not self.origin.isNull():
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.rubberBand.hide()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Window()
    window.resize(2160, 1440)
    window.showFullScreen()
    window.setWindowOpacity(0.3)
    window.repaint()
    qpal = QPalette()
    qpal.setBrush(QPalette.Highlight, QBrush(Qt.red))
    window.rubberBand.setPalette(qpal)
    window.show()
    sys.exit(app.exec_())
