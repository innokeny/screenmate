import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap

class ScreenMate(QLabel):
    def __init__(self):
        super().__init__()

        # Настройка прозрачного окна без рамки
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        # Перемещение скринмейта по экрану
        self.drag_position = None
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.drag_position:
            new_pos = event.globalPos() - self.drag_position
            self.move(self.get_clamped_position(new_pos))

    def mouseReleaseEvent(self, event):
        self.drag_position = None

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            QApplication.instance().quit()

    def get_clamped_position(self, pos):
        screen_rect = QApplication.desktop().availableGeometry()

        # Ограничения для новых координат
        x = min(max(pos.x(), screen_rect.left()), screen_rect.right() - self.width())
        y = min(max(pos.y(), screen_rect.top()), screen_rect.bottom() - self.height())

        return QPoint(x, y)
