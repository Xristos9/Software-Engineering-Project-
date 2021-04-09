# This is the UI for the Login
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(290, 160, 441, 411))
        self.groupBox.setStyleSheet("background-color:rgba(126,156,209,255)\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditusername = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditusername.setObjectName("lineEditusername")
        self.horizontalLayout.addWidget(self.lineEditusername)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditpassword = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditpassword.setObjectName("lineEditpassword")
        self.horizontalLayout_2.addWidget(self.lineEditpassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login = QtWidgets.QPushButton(self.groupBox)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.Noacc = QtWidgets.QLabel(self.groupBox)
        self.Noacc.setObjectName("Noacc")
        self.verticalLayout.addWidget(self.Noacc)
        self.log_with = QtWidgets.QLabel(self.groupBox)
        self.log_with.setObjectName("log_with")
        self.verticalLayout.addWidget(self.log_with)
        self.facebook = QtWidgets.QPushButton(self.groupBox)
        self.facebook.setObjectName("facebook")
        self.verticalLayout.addWidget(self.facebook)
        self.gmail = QtWidgets.QPushButton(self.groupBox)
        self.gmail.setObjectName("gmail")
        self.verticalLayout.addWidget(self.gmail)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setObjectName("actionView")
        self.menuFile.addAction(self.actionView)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BookAll"))
        self.label_4.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Log In"))
        self.Noacc.setText(_translate("MainWindow", "Don\'t Have An Account?"))
        self.log_with.setText(_translate("MainWindow", "Login with"))
        self.facebook.setText(_translate("MainWindow", "facebook"))
        self.gmail.setText(_translate("MainWindow", "gmail"))
        self.menuFile.setTitle(_translate("MainWindow", "File "))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionView.setText(_translate("MainWindow", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
