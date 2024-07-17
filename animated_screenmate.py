from PyQt5.QtCore import QTimer, QPoint, Qt
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QLabel
from screenmate import ScreenMate
from ai_logic import choose_action, move_relative_to_mouse

class AnimatedScreenMate(ScreenMate):
    def __init__(self):
        super().__init__()

        # Загрузка GIF-анимации
        self.mRight = QMovie("character/100h_r.gif")
        self.mLeft = QMovie("character/100h_l.gif")
        self.mUp = QMovie("character/100h_u.gif")
        self.mDown = QMovie("character/100h_d.gif")
        self.mStand = QMovie("character/100h_afk.gif")
        self.mTalk = QMovie("character/100h_talk.gif")

        self.movie = self.mStand
        self.mode = 'stand'

        # Создание таймера для выбора действия ИИ
        self.action_timer = QTimer(self)
        self.action_timer.timeout.connect(lambda: choose_action(self))
        self.action_timer.start(2000)

        # Создание таймера для анимации движения
        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.animate)

        # Таймер для отслеживания курсора мыши
        self.mouse_timer = QTimer(self)
        self.mouse_timer.timeout.connect(self.update_mode)
        self.mouse_timer.start(100)

        # Установка первоначального изображения
        self.setMovie(self.mStand)
        self.movie.start()

    def set_talking_mode(self, talking):
        if talking:
            self.set_mode('talk')
        else:
            self.set_mode('stand')

    def set_mode(self, mode):
        self.mode = mode
        if self.mode == 'talk':
            self.action_timer.stop()
            self.movie = self.mTalk
        elif self.mode == 'stand':
            self.movie = self.mStand
            self.action_timer.start(2000)
        self.setMovie(self.movie)
        self.movie.start()

    def start_moving(self):
        self.movie.start()
        self.move_timer.start(100)
        print(f"Начало движения в направлении: {self.get_direction()}")

    def stop_moving(self):
        self.move_timer.stop()
        self.movie.stop()
        self.setMovie(self.mStand)
        self.movie.start()
        print("Остановка движения")

    def animate(self):
        current_pos = self.pos()
        if self.movie == self.mRight:
            new_pos = QPoint(current_pos.x() + 10, current_pos.y())
        elif self.movie == self.mLeft:
            new_pos = QPoint(current_pos.x() - 10, current_pos.y())
        elif self.movie == self.mUp:
            new_pos = QPoint(current_pos.x(), current_pos.y() - 10)
        elif self.movie == self.mDown:
            new_pos = QPoint(current_pos.x(), current_pos.y() + 10)
        else:
            new_pos = current_pos  # Если анимация не двигается, остаемся на текущей позиции

        self.move(self.get_clamped_position(new_pos))
        print(f"Moved to: {new_pos}")

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
