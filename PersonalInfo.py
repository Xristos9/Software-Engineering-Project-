# This is the UI for the Personal Information Page
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 40, 491, 511))
        self.groupBox.setStyleSheet("background-color:rgb(64, 255, 160)")
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(180, 30, 104, 41))
        self.textEdit.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 110, 161, 71))
        self.textEdit_2.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 180, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 290, 131, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 320, 131, 20))
        self.lineEdit_3.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170, 350, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(320, 350, 47, 13))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 410, 101, 41))
        self.pushButton.setStyleSheet("background-color:rgb(255, 176, 49)")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(160, 370, 274, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout.addWidget(self.lineEdit_8)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(170, 210, 135, 67))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.widget2 = QtWidgets.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(50, 480, 371, 25))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setStyleSheet("background-color:rgb(84, 130, 255)\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_4.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_5.setStyleSheet("background-color:rgb(84, 130, 255)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate(
            "MainWindow", "Personal Information"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BookAll</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Παρακαλώ εισάγετε τα προσωπικά σας στοιχεία</p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "Ονοματεπώνυμα Επιβατών"))
        self.label_3.setText(_translate("MainWindow", "Τηλέφωνο"))
        self.label_7.setText(_translate("MainWindow", "Ενήλικες"))
        self.label_9.setText(_translate("MainWindow", "Ανήλικοι"))
        self.pushButton.setText(_translate("MainWindow", "Κάνε Κράτηση"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.pushButton_4.setText(_translate("MainWindow", "Favourites"))
        self.pushButton_5.setText(_translate("MainWindow", "Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
