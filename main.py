import sys
from PyQt5.QtWidgets import QApplication
from animated_screenmate import AnimatedScreenMate
from voice_assistant.app import main

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание и отображение скринмейта
    screen_mate = AnimatedScreenMate()
    screen_mate.show()

    main()

    sys.exit(app.exec_())
