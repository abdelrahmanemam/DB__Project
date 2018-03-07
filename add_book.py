#from __future__ import print_function
#import cx_Oracle
###################################
###################################
import sys 
from PyQt5 import QtWidgets,QtGui


#connection = cx_Oracle.connect('system/bedouoch123@localhost/library')
#cur = connection.cursor()
text=[0,1,2,3,4,5]

class addbookcls (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,500)
        self.addbook()

    def addbook(self):

        l=[0,1,2,3,4,5]
        w=QtWidgets.QWidget()
        self.centralwidget=QtWidgets.QWidget(w)
        self.setWindowTitle('Library')
        

        mnlbl=QtWidgets.QLabel()
        mnlbl.setText('Add Books')
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
        l[1].setText('ISBN')
        self.le1 = QtWidgets.QLineEdit()
        l[2].setText('Auther ID')
        self.le2 = QtWidgets.QLineEdit()
        l[3].setText('Year')
        self.le3 = QtWidgets.QLineEdit()
        l[4].setText('Title')
        self.le4 = QtWidgets.QLineEdit()
        l[5].setText('Price')
        self.le5 = QtWidgets.QLineEdit()

        bck_btn=QtWidgets.QPushButton('Exit')

        bsh_btn=QtWidgets.QPushButton('Add Book')
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
        vbox.addWidget(l[5])
        vbox.addWidget(self.le5)
        vbox.addWidget(bsh_btn)
        vbox.addWidget(bck_btn)

        self.setLayout(vbox)
        #bsh_btn.clicked.connect(self.add_book)
        
        bck_btn.clicked.connect(self.to_admin)
       
        
        self.show()

    def to_admin(self):
        from admin_sec import admin_window
        window1=admin_window()

        self.hide()
    def add_book(self):
        text[0] =self.le0.text()
        text[1] =self.le1.text()
        text[2] =self.le2.text()
        text[3] =self.le3.text()
        text[4] =self.le4.text()
        text[5] =self.le5.text()
        rows = [((1,text[0]),(2,text[1]),(3,text[2]),(4,text[3]),(5,text[5]))]
        cur.bindarraysize = len(rows)
        print(text[0],'\n',text[1],'\n',text[2],'\n',text[3],'\n',text[4],'\n',text[5],'\n')

        cur.executemany("INSERT INTO BOOK (BOOK_ID,ISBN,AUTHOR_ID,YEAR,TITLLE,PRICE) VALUES(:1,:2,:3,:4,char,:5)",rows)

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    window1=addbookcls()
    window1.addbook()
    w.show()
    window1=admin_window()
    sys.exit(app.exec_())

