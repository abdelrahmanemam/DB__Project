#from __future__ import print_function
#import cx_Oracle
####################################
import sys 
from PyQt5 import QtWidgets,QtGui
from add_book import addbookcls
from return_book import returnbookcls
from issue_book import issuebookcls
from view_book import viewbookcls

#connection = cx_Oracle.connect('system/bedouoch123@localhost/library')
#cur = connection.cursor()

class admin_window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(300,300)
        
        self.admin_sec()

    def admin_sec(self):
    	

        w1=QtWidgets.QWidget()	
        self.centralwidget=QtWidgets.QWidget(w1)
        self.setWindowTitle('Library')

        l1=QtWidgets.QLabel()
        l1.setText('Admin Section')
        font1=QtGui.QFont()
        font1.setPointSize(25)
        l1.setFont(font1)

        b1=QtWidgets.QPushButton('Add Books')
        b2=QtWidgets.QPushButton('View Books')
        b3=QtWidgets.QPushButton('Borrow Book')
        b4=QtWidgets.QPushButton('Return Book')
        b5=QtWidgets.QPushButton('Logout')
        b6=QtWidgets.QPushButton('Exit')

        font=QtGui.QFont()
        font.setPointSize(10)
        
        b1.setFont(font)
        b2.setFont(font)
        b3.setFont(font)
        b4.setFont(font)
        b5.setFont(font)
        b6.setFont(font)

        hbox=QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(l1)
        hbox.addStretch()

        vbox=QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)


        vbox.addWidget(b1)
        vbox.addWidget(b2)
        vbox.addWidget(b3)
        vbox.addWidget(b4)
        vbox.addWidget(b5)
        vbox.addWidget(b6)



        self.setLayout(vbox)

        self.show()

        b1.clicked.connect(self.add_books_popup)
        b2.clicked.connect(self.view_books_popup)
        b3.clicked.connect(self.issue_books_popup)
        b4.clicked.connect(self.return_books_popup)
        b6.clicked.connect(self.Exit)

    def add_books_popup(self):
        self.window=QtWidgets.QMainWindow()
        self.window1= addbookcls()
        self.window1.addbook()
        #window1.hide()

    def return_books_popup(self):
        self.window=QtWidgets.QMainWindow()
        self.window1= returnbookcls()
        self.window1.returnbook()
        #window1.hide()    

    def issue_books_popup(self):
        self.window=QtWidgets.QMainWindow()
        self.window1= issuebookcls()
        self.window1.issuebook()
        #window1.hide()

    def view_books_popup(self):
        self.window=QtWidgets.QMainWindow()
        self.window1= viewbookcls()
        self.window1.view_book()

    def Exit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    window1=admin_window()
    window1.admin_sec()
    w1.show()
    window1=admin_window()
    sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    w1=QtWidgets.QMainWindow()
    window1=addbookcls()
    window1.addbook()
    
    window1=admin_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    w1=QtWidgets.QMainWindow()
    window1=returnbookcls()
    window1.returnbook()
    
    window1=admin_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    w1=QtWidgets.QMainWindow()
    window1=issuebookcls()
    window1.issuebook()
    
    window1=admin_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    w1=QtWidgets.QMainWindow()
    window1=viewbookcls()
    window1.viewbook()
    
    window1=admin_window()
    sys.exit(app.exec_())