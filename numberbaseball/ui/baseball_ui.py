# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numberBaseball.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NumberBaseball(object):
    def setupUi(self, NumberBaseball):
        NumberBaseball.setObjectName("NumberBaseball")
        NumberBaseball.resize(338, 531)
        self.centralwidget = QtWidgets.QWidget(NumberBaseball)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLabel.sizePolicy().hasHeightForWidth())
        self.inputLabel.setSizePolicy(sizePolicy)
        self.inputLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.inputLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        self.inputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLabel.setObjectName("inputLabel")
        self.verticalLayout.addWidget(self.inputLabel)
        self.InputTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputTextEdit.sizePolicy().hasHeightForWidth())
        self.InputTextEdit.setSizePolicy(sizePolicy)
        self.InputTextEdit.setMinimumSize(QtCore.QSize(300, 50))
        self.InputTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.InputTextEdit.setText("")
        self.InputTextEdit.setMaxLength(3)
        self.InputTextEdit.setObjectName("InputTextEdit")
        self.verticalLayout.addWidget(self.InputTextEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 60))
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout.addWidget(self.submitButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setMinimumSize(QtCore.QSize(0, 60))
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)
        self.checkoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkoutButton.setMinimumSize(QtCore.QSize(0, 60))
        self.checkoutButton.setObjectName("checkoutButton")
        self.verticalLayout.addWidget(self.checkoutButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        NumberBaseball.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NumberBaseball)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 26))
        self.menubar.setObjectName("menubar")
        NumberBaseball.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NumberBaseball)
        self.statusbar.setObjectName("statusbar")
        NumberBaseball.setStatusBar(self.statusbar)

        self.retranslateUi(NumberBaseball)
        QtCore.QMetaObject.connectSlotsByName(NumberBaseball)

    def retranslateUi(self, NumberBaseball):
        _translate = QtCore.QCoreApplication.translate
        NumberBaseball.setWindowTitle(_translate("NumberBaseball", "MainWindow"))
        self.inputLabel.setText(_translate("NumberBaseball", "<p style=\"font-size:18px; font-family:Arial;\">\n"
"숫자를 입력해 주세요. <br> 숫자는 중복되면 안됩니다.\n"
"</p>"))
        self.label_2.setText(_translate("NumberBaseball", "<p style=\"font-size:18px; font-family:Arial;\">\n"
"결과는 다음과 같습니다.\n"
"</p>"))
        self.submitButton.setText(_translate("NumberBaseball", "Submit"))
        self.resetButton.setText(_translate("NumberBaseball", "Reset"))
        self.checkoutButton.setText(_translate("NumberBaseball", "Check out the answer"))

