#from __future__ import print_function
#import cx_Oracle
####################################
import sys 
from PyQt5 import QtWidgets,QtGui
 


class viewbookcls(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(450,400)
        
        self.view_book()

    def view_book(self):
        w1=QtWidgets.QWidget()	
        self.centralwidget=QtWidgets.QWidget(w1)
        self.setWindowTitle('Library')

        b1=QtWidgets.QPushButton('View Books')
        b2=QtWidgets.QPushButton('Exit')

        font=QtGui.QFont()
        font.setPointSize(10)

        b1.setFont(font)
        b2.setFont(font)

       	text=QtWidgets.QTextEdit(self)

       	vbox=QtWidgets.QVBoxLayout()
       	vbox.addWidget(text)
        vbox.addWidget(b1)
        vbox.addWidget(b2)
        

        self.setLayout(vbox)

        self.show()

       	#b1.clicked.connect(self.view_books)
        b2.clicked.connect(self.to_admin)

    # def view_books(self):
    #     connection = cx_Oracle.connect('system/bedouoch123@localhost/library')
    #     cur = connection.cursor()

    #     cur.execute('select * from Book ' )

    #     rows=cur.fetchall()
    #     text1=QtWidgets.QTextEdit(self)
    #     with open('text.txt','r+') as f:
    #     	text1.append(str(rows))
    #     	text1.show()
    #     	f.write(str(rows))
        	
    #     	# file1=f.read()
    #     	# print(str(file1))
    #     	# text1.append(str(file1))
	   #      # name= QtWidgets.QFileDialog.getOpenFileName(self,'open file','text.txt')
	   #      # file= open(str(text),'r')
	   #      # with file:
	   #      # 	text=file.read()
	   #      # 	self.textEdit.SetText(text)			

    #     cur.close()

    #     connection.close()


       
    def to_admin(self):
    	self.hide()

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    window1=viewbookcls()
    window1.view_book()
    w.show()
    window1=admin_window()
    sys.exit(app.exec_())

