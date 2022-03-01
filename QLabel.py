import sys
from PyQt5.QtWidgets import QVBoxLayout,QApplication,QMainWindow,QLabel,QWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class QLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)

        label1.linkHovered.connect(self.linkHovered)
        label2.linkClicked.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel演示')


    def linkHovered(self):
        print('当鼠标滑过label1时触发')

    def linkClicked(self):
        print('当鼠标单击label2时触发')


if __name__=='__main__':

    app = QApplication(sys.argv)

    main = QLabel()
    main.show()
    sys.exit(app.exec_())