import sys

from PyQt5 import QtWidgets,QtGui

#Python etiket oluşturma
def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("images/python.png"))

    etiket1.setText("<strong>Python PyQt5</strong>")
    etiket1.move(200,30)
    etiket2.move(80,100)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()


