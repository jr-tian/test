import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class DrawTest(QWidget):
    def __init__(self):
        super(DrawTest,self).__init__()
        
        self.setWindowTitle('绘制文本')
        self.resize(300,200)
        self.text = 'Py'
    
    def paintEvent(self, event):
        painter= QPainter()
        painter.begin(self)

        painter.setPen(QColor(150,143,5))
        painter.setFont(QFont('SimSun',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawTest()
    main.show()
    sys.exit(app.exec_())