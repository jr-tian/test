import sys
import Ui_untitled

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui=Ui_untitled.Ui_MainWindow()
    
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
