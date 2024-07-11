import sys
from PyQt5.QtWidgets import QApplication
from animated_screenmate import AnimatedScreenMate

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание и отображение скринмейта
    screen_mate = AnimatedScreenMate()
    screen_mate.show()

    sys.exit(app.exec_())
