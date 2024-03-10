# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 567)
        MainWindow.setStyleSheet("background:rgb(0, 0, 0) ;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 0, 451, 31))
        self.title.setStyleSheet("border :2px solid white;\n"
"border-radius: 10px ;")
        self.title.setObjectName("title")
        self.texp = QtWidgets.QTextEdit(self.centralwidget)
        self.texp.setGeometry(QtCore.QRect(10, 40, 451, 481))
        self.texp.setStyleSheet("border :2px solid white;\n"
"border-radius: 10px ;")
        self.texp.setObjectName("texp")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(480, 250, 111, 31))
        self.create_btn.setStyleSheet("border :2px solid white;")
        self.create_btn.setObjectName("create_btn")
        self.listteg = QtWidgets.QListView(self.centralwidget)
        self.listteg.setGeometry(QtCore.QRect(480, 340, 251, 121))
        self.listteg.setStyleSheet("border :2px solid white;\n"
"border-radius: 10px ;")
        self.listteg.setObjectName("listteg")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(480, 290, 231, 41))
        self.save_btn.setStyleSheet("border :2px solid white;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255))")
        self.save_btn.setObjectName("save_btn")
        self.deletezam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.deletezam_btn.setGeometry(QtCore.QRect(600, 250, 111, 31))
        self.deletezam_btn.setStyleSheet("border :2px solid white;")
        self.deletezam_btn.setObjectName("deletezam_btn")
        self.gbereggam_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gbereggam_btn.setGeometry(QtCore.QRect(660, 470, 93, 23))
        self.gbereggam_btn.setStyleSheet("border :2px solid white;")
        self.gbereggam_btn.setObjectName("gbereggam_btn")
        self.deleteteg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteteg_btn.setGeometry(QtCore.QRect(660, 500, 97, 23))
        self.deleteteg_btn.setStyleSheet("border :2px solid white;")
        self.deleteteg_btn.setObjectName("deleteteg_btn")
        self.cteateteg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cteateteg_btn.setGeometry(QtCore.QRect(480, 500, 171, 21))
        self.cteateteg_btn.setStyleSheet("border :2px solid white;")
        self.cteateteg_btn.setObjectName("cteateteg_btn")
        self.poisteg = QtWidgets.QLineEdit(self.centralwidget)
        self.poisteg.setGeometry(QtCore.QRect(482, 470, 171, 20))
        self.poisteg.setStyleSheet("border :2px solid white;\n"
"border-radius: 10px ;")
        self.poisteg.setObjectName("poisteg")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(470, 40, 256, 192))
        self.listWidget.setStyleSheet("border :2px solid white;\n"
"border-radius: 10px ;")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EASY SUPER PAVER TROLEIBES"))
        self.title.setPlaceholderText(_translate("MainWindow", "Ведіть назву "))
        self.create_btn.setText(_translate("MainWindow", "Створіти замітку"))
        self.save_btn.setText(_translate("MainWindow", "Зберешти замітку"))
        self.deletezam_btn.setText(_translate("MainWindow", "Видалити замітку"))
        self.gbereggam_btn.setText(_translate("MainWindow", "Знайти тег"))
        self.deleteteg_btn.setText(_translate("MainWindow", "Видалити тег"))
        self.cteateteg_btn.setText(_translate("MainWindow", "Створити тег"))
        self.poisteg.setPlaceholderText(_translate("MainWindow", "Ведіть назву тегу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
