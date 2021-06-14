from seat_built import seat_built_detector
from drowsiness_detector import drowsiness_detector
from PyQt5.QtWidgets import  QFormLayout,QPushButton,QGroupBox,QVBoxLayout,QLabel
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
stylesheet = """
    MainWindow {
        background-image: url("D:/back.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setStyleSheet("")
        self.InitWindow()
        self.show()
    def InitWindow(self):
        
        self.pushButton1 = QPushButton("Drowsiness Detection")
        self.pushButton1.setStyleSheet("color:Blue")
        self.pushButton2 = QPushButton("SeatBuilt Detector")
        self.pushButton2.setStyleSheet("color:Blue")
        self.pushButton1.setFont(myFont)
        self.pushButton1.setIconSize(QtCore.QSize(10, 10))
        self.pushButton1.setGeometry(10, 10, 10, 10)
        self.pushButton1.adjustSize()
        self.pushButton2.setFont(myFont)
        self.pushButton2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton2.setGeometry(20, 20, 20, 20)
        self.pushButton1.clicked.connect(drowsiness_detector)
        self.pushButton2.clicked.connect(seat_built_detector)
        self.pushButton2.adjustSize()
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet('''background-image: url("images(2).jpg"); 
        background-repeat: no-repeat; 
        background-position: center;''')
    window = Window()
    window.resize(400, 400)
    window.show()
    window.setStyleSheet(stylesheet)
    sys.exit(app.exec_())

Window()