import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox,self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())

class DrapDrop(QWidget):
    def __init__(self):
        super(DrapDrop,self).__init__()

        self.setWindowTitle('拖拽案例')

        formLayout = QFormLayout()
        formLayout.addRow(QLabel('拖拽文本'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)

        combo = MyComboBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDrop()
    main.show()
    sys.exit(app.exec_())