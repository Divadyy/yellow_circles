import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.uic import loadUi


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        x = random.randint(0, self.width() - 50)
        y = random.randint(0, self.height() - 50)
        diameter = random.randint(10, 50)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("yellow"), 2)
        painter.setPen(pen)
        painter.setBrush(QColor("yellow"))

        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
