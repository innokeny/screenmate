import sys
from PyQt5.QtWidgets import QApplication
from animated_screenmate import AnimatedScreenMate
from voice_assistant.app import recognize as voice_assistant_recognize
from PyQt5.QtCore import QTimer, Qt
import threading

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание и отображение скринмейта
    screen_mate = AnimatedScreenMate()
    screen_mate.show()

    # Таймер для запуска голосового ассистента по клику
    voice_timer = QTimer()
    
    # Сохранение оригинального метода
    original_mousePressEvent = screen_mate.mousePressEvent

    def handle_click(event):
        if event.button() == Qt.RightButton:
            screen_mate.set_mode('talk')
            def start_voice_assistant():
                voice_assistant_recognize(screen_mate)
                screen_mate.set_mode('stand')
            threading.Thread(target=start_voice_assistant, daemon=True).start()
        elif event.button() == Qt.LeftButton:
            original_mousePressEvent(event)  # вызов оригинального метода для перемещения

    screen_mate.mousePressEvent = handle_click

    sys.exit(app.exec_())
