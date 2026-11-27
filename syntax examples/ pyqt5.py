import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI")
        self.setGeometry(500,200,500,500)
        self.setWindowIcon(QIcon("pyicon.png"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Helvetica", 40))
        label.setGeometry(0,0,500,500)
        label.setStyleSheet("color: #247038;"
                            "background-color: #edf5ef;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignmentFlag.AlignTop) #Vertically top
        #label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        #label.setAlignment(Qt.AlignmentFlag.AlignVCenter) #Vertically vertically centerd
        #label.setAlignment(Qt.AlignmentFlag.AlignRight)
        #label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #label.setAlignment(Qt.AlignmentFlag.AlignHCenter) #Horizontally centerd
        #label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_pic = QLabel(self)
        label_pic.setGeometry(0,0,250,250)
        pixmap = QPixmap("pyicon.png")
        label_pic.setPixmap(pixmap)
        label_pic.setScaledContents(True)
        label_pic.setGeometry((self.width() - label_pic.width()) // 2,
                              (self.height() - label_pic.height()) // -2,
                              label_pic.width(),
                              label_pic.height())


def main():
    app = QApplication(sys.argv) #allows for processing cli arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()