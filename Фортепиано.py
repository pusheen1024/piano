import sys
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSound
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class AudioButton(QPushButton):
    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sound = QSound(filename)
        self.clicked.connect(self.sound.play)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Фортепиано')
        self.setGeometry(300, 300, 700, 170)
        start_coords_white, cur = (5, 10), 0
        self.buttons = list()
        for octave in range(3, 7):
            for pitch in 'ABCDEFG' if octave > 3 else 'AB':
                filename = f'./violin/violin_{pitch}{octave}_05_forte_arco-normal.wav'
                button = AudioButton(filename, self)
                button.resize(30, 150)
                button.move(start_coords_white[0] + cur * 30, start_coords_white[1])
                self.buttons.append(button)
                cur += 1
        # black buttons do not perform any functions, they are simply here to create a picture of a piano
        button = QPushButton(self)
        button.resize(15, 75)
        button.move(28, 10)
        button.setStyleSheet('background-color: #000000')
        start_coords_black = (88, 10)
        for pos in range(21):
            if pos % 7 in (2, 6):
                continue
            button = QPushButton(self)
            button.resize(15, 75)
            button.move(start_coords_black[0] + pos * 30, start_coords_black[1])
            button.setStyleSheet('background-color: #000000')

    def keyPressEvent(self, event):
        if Qt.Key_A <= event.key() <= Qt.Key_G:
            num = event.key() - Qt.Key_A
            if int(event.modifiers()) == Qt.AltModifier:
                self.buttons[2 + num].clicked.emit()
            elif int(event.modifiers()) == Qt.ControlModifier:
                self.buttons[9 + num].clicked.emit()
            elif int(event.modifiers()) == Qt.ShiftModifier:
                self.buttons[16 + num].clicked.emit()
            elif num < 2:
                self.buttons[num].clicked.emit()
            
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
