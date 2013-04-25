# UI file for my BTP.
# Source Code written by Harsh Shah

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
#       MainWindow.resize(945, 488)
#	MainWindow.setGeometry(230,130,900,500) 
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(440, 50, 141, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(650, 50, 131, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(640, 100, 151, 241))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEdit_9 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.verticalLayout_4.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.verticalLayout_4.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.verticalLayout_4.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.verticalLayout_4.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.verticalLayout_4.addWidget(self.lineEdit_13)
        self.lineEdit_14 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.verticalLayout_4.addWidget(self.lineEdit_14)
        self.lineEdit_15 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.verticalLayout_4.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.verticalLayout_4.addWidget(self.lineEdit_16)
        self.layoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(430, 100, 146, 241))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.verticalLayout_5.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.verticalLayout_5.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.verticalLayout_5.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.verticalLayout_5.addWidget(self.lineEdit_8)
        self.layoutWidget_4 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(280, 100, 134, 231))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_14 = QtGui.QLabel(self.layoutWidget_4)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_6.addWidget(self.label_14)
        self.label_17 = QtGui.QLabel(self.layoutWidget_4)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_24 = QtGui.QLabel(self.layoutWidget_4)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_6.addWidget(self.label_24)
        self.label_25 = QtGui.QLabel(self.layoutWidget_4)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_6.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(self.layoutWidget_4)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout_6.addWidget(self.label_26)
        self.label_27 = QtGui.QLabel(self.layoutWidget_4)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.verticalLayout_6.addWidget(self.label_27)
        self.label_28 = QtGui.QLabel(self.layoutWidget_4)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_6.addWidget(self.label_28)
        self.label_29 = QtGui.QLabel(self.layoutWidget_4)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.verticalLayout_6.addWidget(self.label_29)
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 410, 91, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_19 = QtGui.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(60, 180, 141, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 360, 91, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 210, 121, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.toolButton = QtGui.QToolButton(self.centralWidget)
        self.toolButton.setGeometry(QtCore.QRect(190, 210, 25, 21)) 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 945, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuHowTo = QtGui.QMenu(self.menuBar)
        self.menuHowTo.setObjectName(_fromUtf8("menuHowTo"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuHowTo.addAction(self.actionHelp)
        self.menuBar.addAction(self.menuHowTo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Strategy Analyzer", None))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Welcome to Harsh\'s BTP!</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Call Option Details", None))
        self.label_2.setText(_translate("MainWindow", "Put Option Details", None))
        self.label_14.setText(_translate("MainWindow", "Buying Price - 1       ", None))
        self.label_17.setText(_translate("MainWindow", "Strike Price       ", None))
        self.label_24.setText(_translate("MainWindow", "Buying Price - 2       ", None))
        self.label_25.setText(_translate("MainWindow", "Strike Price       ", None))
        self.label_26.setText(_translate("MainWindow", "Selling Price - 1       ", None))
        self.label_27.setText(_translate("MainWindow", "Strike Price      ", None))
        self.label_28.setText(_translate("MainWindow", "Selling Price - 2    ", None))
        self.label_29.setText(_translate("MainWindow", "Strike Price    ", None))
        self.pushButton_2.setText(_translate("MainWindow", "Show Result", None))
        self.label_19.setText(_translate("MainWindow", "Select Your Strategy", None))
        self.pushButton.setText(_translate("MainWindow", "Freeze", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Bull Spread", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bear Spread", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Box Spread", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Butterfly Spread", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Straddle", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "Strips", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "Straps", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "Strangle", None))
        self.menuHowTo.setTitle(_translate("MainWindow", "HowTo", None))
        self.actionHelp.setText(_translate("MainWindow", "Help !", None))

