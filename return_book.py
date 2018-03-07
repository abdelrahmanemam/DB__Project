#from __future__ import print_function
#import cx_Oracle
###################################
###################################
import sys 
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QFont, QPalette

#connection = cx_Oracle.connect('system/bedouoch123@localhost/library')
#cur = connection.cursor()
text=[0,1]



class returnbookcls (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,250)
        self.returnbook()

    def returnbook(self):
        l=[0,1]
        w=QtWidgets.QWidget()
        self.centralwidget=QtWidgets.QWidget(w)
        self.setWindowTitle('Library')

        mnlbl=QtWidgets.QLabel()
        mnlbl.setText('Return Book')
        font1=QtGui.QFont()
        font1.setPointSize(25)
        mnlbl.setFont(font1)
        i=0
        while i<2:
            l[i]=QtWidgets.QLabel()
            i=i+1
        font=QtGui.QFont()
        font.setPointSize(10)
        l[0].setFont(font)
        l[1].setFont(font)


        l[0].setText('Book ID')
        self.le0 = QtWidgets.QLineEdit()
        l[1].setText('Borrower ID')


        self.le1 = QtWidgets.QLineEdit()
        m = QtWidgets.QWidget()

        bck_btn=QtWidgets.QPushButton('Exit')

        bsh_btn=QtWidgets.QPushButton('Return Book')
        font2=QtGui.QFont()
        font2.setPointSize(13)
        bsh_btn.setFont(font2)

        hbox=QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(mnlbl)
        hbox.addStretch()


        vbox=QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(l[0])
        vbox.addWidget(self.le0)
        vbox.addWidget(l[1])
        vbox.addWidget(self.le1)
        vbox.addWidget(bsh_btn)
        vbox.addWidget(bck_btn)

        self.setLayout(vbox)
        #bsh_btn.clicked.connect(self.return_book)
        bck_btn.clicked.connect(self.to_admin)
       
        
        self.show()

    def to_admin(self):
        from admin_sec import admin_window
        window1=admin_window()

        self.hide()
    # def return_book(self):

    #     text[0] =self.le0.text()
    #     text[1] =self.le1.text()
        

    #     cur.execute("""INSERT INTO RETURNED_BOOK (BOOK_ID,BORROWER_ID) VALUES(text[0],text[1])""")



if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    window1=returnbookcls()
    window1.returnbook()
    w.show()
    window1=admin_window()
    sys.exit(app.exec_())

