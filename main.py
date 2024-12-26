import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.button = QPushButton("Draw Circle", self)
        self.button.setGeometry(225, 350, 150, 30)
        self.button.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        radius = random.randint(10, 50)
        x = random.randint(radius, self.width() - radius)
        y = random.randint(radius, self.height() - radius)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, radius, color in self.circles:
            pen = QPen(color, 2)
            brush = QBrush(color)
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
