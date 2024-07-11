# animated_screenmate.py
from PyQt5.QtCore import QTimer, QPoint, Qt
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QLabel
from screenmate import ScreenMate
from ai_logic import choose_action, move_relative_to_mouse

class AnimatedScreenMate(ScreenMate):
    def __init__(self):
        super().__init__()

        # Загрузка GIF-анимации
        self.mRight = QMovie("100_r.gif")
        self.mLeft = QMovie("100_l.gif")
        self.mUp = QMovie("100_r.gif")
        self.mDown = QMovie("100_l.gif")

        # Начальная анимация (можно выбрать любую)
        self.movie = self.mRight
        self.mode = 'stand'

        # Создание таймера для выбора действия ИИ
        self.action_timer = QTimer(self)
        self.action_timer.timeout.connect(lambda: choose_action(self))
        self.action_timer.start(2000)  # Интервал в миллисекундах для выбора действия

        # Создание таймера для анимации движения
        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.animate)

        # Таймер для отслеживания курсора мыши
        self.mouse_timer = QTimer(self)
        self.mouse_timer.timeout.connect(self.update_mode)
        self.mouse_timer.start(100)  # Интервал в миллисекундах для отслеживания курсора

    def start_moving(self):
        self.movie.start()
        self.move_timer.start(100)  # Интервал в миллисекундах для анимации
        print(f"Начало движения в направлении: {self.get_direction()}")

    def stop_moving(self):
        self.move_timer.stop()
        self.movie.stop()
        self.setPixmap(self.static_pixmap)
        print("Остановка движения")

    def animate(self):
        # Пример простой анимации: перемещение скринмейта в зависимости от установленной анимации
        current_pos = self.pos()
        if self.movie == self.mRight:
            new_pos = QPoint(current_pos.x() + 10, current_pos.y())
        elif self.movie == self.mLeft:
            new_pos = QPoint(current_pos.x() - 10, current_pos.y())
        elif self.movie == self.mUp:
            new_pos = QPoint(current_pos.x(), current_pos.y() - 10)
        elif self.movie == self.mDown:
            new_pos = QPoint(current_pos.x(), current_pos.y() + 10)

        self.move(self.get_clamped_position(new_pos))
        print(f"Moved to: {new_pos}")  # Отладочное сообщение

    def get_direction(self):
        if self.movie == self.mRight:
            return 'right'
        elif self.movie == self.mLeft:
            return 'left'
        elif self.movie == self.mUp:
            return 'up'
        elif self.movie == self.mDown:
            return 'down'
        else:
            return 'stand'

    def update_mode(self):
        if self.mode == 'evade':
            move_relative_to_mouse(self, chase=False)
        elif self.mode == 'chase':
            move_relative_to_mouse(self, chase=True)




        # self.mRight = QMovie("100_r.gif")
        # self.mLeft = QMovie("100_l.gif")
        # self.mUp = QMovie("100_r.gif")
        # self.mDown = QMovie("100_l.gif")