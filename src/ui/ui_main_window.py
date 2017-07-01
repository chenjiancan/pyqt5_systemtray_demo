# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBoxIsShowTray = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxIsShowTray.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBoxIsShowTray.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxIsShowTray.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxIsShowTray.setObjectName("buttonBoxIsShowTray")
        self.checkBoxIsShowTray = QtWidgets.QCheckBox(Dialog)
        self.checkBoxIsShowTray.setGeometry(QtCore.QRect(110, 50, 171, 21))
        self.checkBoxIsShowTray.setObjectName("checkBoxIsShowTray")

        self.retranslateUi(Dialog)
        self.buttonBoxIsShowTray.accepted.connect(Dialog.accept)
        self.buttonBoxIsShowTray.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBoxIsShowTray.setText(_translate("Dialog", "show tray?"))

