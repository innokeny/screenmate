import sys
from PyQt5.QtWidgets import QApplication
from animated_screenmate import AnimatedScreenMate
from voice_assistant.app import recognize as voice_assistant_recognize
from PyQt5.QtCore import QTimer, Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание и отображение скринмейта
    screen_mate = AnimatedScreenMate()
    screen_mate.show()

    # Таймер для запуска голосового ассистента по клику
    voice_timer = QTimer()
    voice_timer.timeout.connect(lambda: voice_assistant_recognize(screen_mate))
    
    def handle_click(event):
        if event.button() == Qt.LeftButton:
            voice_timer.start(1000)  # запуск голосового помощника по клику на скринмейта

    screen_mate.mousePressEvent = handle_click

    sys.exit(app.exec_())
