import sys 
from PyQt5 import QtWidgets,QtGui
from admin_sec import admin_window

class window (QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(250,260)
        self.init_ui()
        

    def init_ui(self):
        w=QtWidgets.QWidget()
        self.centralwidget=QtWidgets.QWidget(w)
        

        self.setWindowTitle('Library')

        main_lb=QtWidgets.QLabel()
        main_lb.setText('Admin Login form')
        font1=QtGui.QFont()
        font1.setPointSize(20)
        main_lb.setFont(font1)



        l1=QtWidgets.QLabel()
        l1.setText('Enter Name:')
        self.le1 = QtWidgets.QLineEdit()

        l2=QtWidgets.QLabel()
        l2.setText('Enter Password:')
        self.le2 = QtWidgets.QLineEdit()


        admn_bt=QtWidgets.QPushButton('Login')
        font=QtGui.QFont()
        font.setPointSize(10)
        admn_bt.setFont(font)

        Exit_bt=QtWidgets.QPushButton('Exit')
        font=QtGui.QFont()
        font.setPointSize(10)
        Exit_bt.setFont(font)


        hbox=QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(main_lb)
        hbox.addStretch()


        vbox=QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(l1)
        vbox.addWidget(self.le1)
        vbox.addWidget(l2)
        vbox.addWidget(self.le2)
        vbox.addWidget(admn_bt)
        vbox.addWidget(Exit_bt)

        font=QtGui.QFont()
        font.setPointSize(25)

        self.setLayout(vbox)
        admn_bt.clicked.connect(self.openwindow)
        Exit_bt.clicked.connect(self.Exit)

        self.show()

    def openwindow (self):
        #self.window=QtWidgets.QMainWindow()
        self.window1= admin_window()
        self.window1.admin_sec()
        window1.hide()

    def Exit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    w1=QtWidgets.QMainWindow()
    window1=window()
    window1.init_ui()
    
    window1=window()
    sys.exit(app.exec_())

