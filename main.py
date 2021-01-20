import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget




class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.pushButton.setText('OK')
        qp = QPainter(self)
        qp.begin(self)
        self.draw_ellipse(qp)
        qp.end()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(50, 50, 10, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())