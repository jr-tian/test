import sys
from turtle import Screen
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow


class CenterFrom(QMainWindow):
    def __init__(self):
        super(CenterFrom,self).__init__()

        self.setWindowTitle('让屏幕居中')

        self.resize(400,300)
    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2

        self.move(newLeft,newTop)

if __name__=='__main__':

    app = QApplication(sys.argv)

    main = CenterFrom()
    main.show()
    sys.exit(app.exec_())
