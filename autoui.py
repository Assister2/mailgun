# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 459)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 30, 561, 391))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(220, 330, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 340, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.varyNumber = QtWidgets.QCheckBox(self.groupBox)
        self.varyNumber.setGeometry(QtCore.QRect(40, 100, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.varyNumber.setFont(font)
        self.varyNumber.setObjectName("varyNumber")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 340, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.varyRecip = QtWidgets.QCheckBox(self.groupBox)
        self.varyRecip.setGeometry(QtCore.QRect(40, 210, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.varyRecip.setFont(font)
        self.varyRecip.setObjectName("varyRecip")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 491, 91))
        self.label_2.setObjectName("label_2")
        self.dfdf = QtWidgets.QLabel(self.groupBox)
        self.dfdf.setGeometry(QtCore.QRect(60, 220, 491, 91))
        self.dfdf.setObjectName("dfdf")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Automatic Sending"))
        self.groupBox.setTitle(_translate("Dialog", "Auto Mode"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Close"))
        self.varyNumber.setText(_translate("Dialog", "Vary the Phone Number"))
        self.label.setText(_translate("Dialog", "Saved!"))
        self.varyRecip.setText(_translate("Dialog", "Vary the Recipients"))
        self.label_2.setText(_translate("Dialog", "This will change the phone Number to the next number after each Sending\n"
"(Similar to clicking next number)"))
        self.dfdf.setText(_translate("Dialog", "This will change the recipients emails to the next 3 emails after each Sending\n"
"(Similar to clicking Next Emails)"))
        self.label_3.setText(_translate("Dialog", "Enable Automatic Sending"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())