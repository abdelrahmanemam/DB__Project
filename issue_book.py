#from __future__ import print_function
#import cx_Oracle
###################################
###################################
import sys 
from PyQt5 import QtWidgets,QtGui
import os 


#connection = cx_Oracle.connect('system/bedouoch123@localhost/library')
#cur = connection.cursor()
text=[0,1,2,3,4]


class issuebookcls (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,450)
        self.issuebook()

    def issuebook(self):
        l=[0,1,2,3,4,5]
        w=QtWidgets.QWidget()
        self.centralwidget=QtWidgets.QWidget(w)
        self.setWindowTitle('Library')

        mnlbl=QtWidgets.QLabel()
        mnlbl.setText('Borrow Book')
        font1=QtGui.QFont()
        font1.setPointSize(25)
        mnlbl.setFont(font1)
        i=0
        while i<6:
            l[i]=QtWidgets.QLabel()
            i=i+1
        font=QtGui.QFont()
        font.setPointSize(10)
        l[0].setFont(font)
        l[1].setFont(font)
        l[2].setFont(font)
        l[3].setFont(font)
        l[4].setFont(font)
        l[5].setFont(font)

        l[0].setText('Book ID')
        self.le0 = QtWidgets.QLineEdit()
        l[1].setText('Borrower ID')
        self.le1 = QtWidgets.QLineEdit()
        l[2].setText('Received Date')
        self.le2 = QtWidgets.QLineEdit()
        l[3].setText('Return Date')
        self.le3 = QtWidgets.QLineEdit()
        l[4].setText('Borrower Phone no.')
        self.le4 = QtWidgets.QLineEdit()


        bck_btn=QtWidgets.QPushButton('Exit')

        bsh_btn=QtWidgets.QPushButton('Borrow Book')
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
        vbox.addWidget(l[2])
        vbox.addWidget(self.le2)
        vbox.addWidget(l[3])
        vbox.addWidget(self.le3)
        vbox.addWidget(l[4])
        vbox.addWidget(self.le4)
        vbox.addWidget(bsh_btn)
        vbox.addWidget(bck_btn)

        self.setLayout(vbox)

       # bsh_btn.clicked.connect(self.issue_book)
        bck_btn.clicked.connect(self.to_admin)
       
        
        self.show()

    def to_admin(self):
        from admin_sec import admin_window
        window1=admin_window()

        self.hide()



    def issue_book(self):
        text[0] =self.le0.text()
        text[1] =self.le1.text()
        text[2] =self.le2.text()
        text[3] =self.le3.text()
        text[4] =self.le4.text()
        rows = [(text[0],text[1],text[2],text[3])]
        cur.bindarraysize = len(rows)
        #cur.setinputsizes=(cx_Oracle.NUMBER,cx_Oracle.NUMBER,cx_Oracle.DATETIME,cx_Oracle.DATETIME)
        cur.executemany("INSERT INTO BOOK_BORROWER (BOOK_ID,BORROWER_ID,RECEIVED_DATE,RETURN_DATE) VALUES(:1,:2,sysdate,sysdate)",rows)
        rows2=[(text[4])]
        cur.bindarraysize = len(rows)
        #cur.setinputsizes=(int)
        cur.executemany("INSERT INTO BORROWER_PHONE(PHONE)VALUES(:1)",rows2)
        print(text[0],'\n',text[1],'\n',text[2],'\n',text[3],'\n',text[4],'\n')

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    window1=issuebookcls()
    window1.issuebook()
    w.show()
    window1=admin_window()
    sys.exit(app.exec_())


