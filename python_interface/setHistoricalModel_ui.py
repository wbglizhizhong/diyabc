# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/setHistoricalModel.ui'
#
# Created: Mon Jan 10 21:57:10 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 707)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.okButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.verticalLayout_4.addWidget(self.okButton)
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scScroll = QtGui.QScrollArea(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scScroll.sizePolicy().hasHeightForWidth())
        self.scScroll.setSizePolicy(sizePolicy)
        self.scScroll.setMinimumSize(QtCore.QSize(500, 200))
        self.scScroll.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scScroll.setWidgetResizable(True)
        self.scScroll.setObjectName("scScroll")
        self.scScrollContent = QtGui.QWidget(self.scScroll)
        self.scScrollContent.setGeometry(QtCore.QRect(0, 0, 819, 196))
        self.scScrollContent.setObjectName("scScrollContent")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scScrollContent)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scScroll.setWidget(self.scScrollContent)
        self.horizontalLayout_5.addWidget(self.scScroll)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addScButton = QtGui.QPushButton(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addScButton.sizePolicy().hasHeightForWidth())
        self.addScButton.setSizePolicy(sizePolicy)
        self.addScButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.addScButton.setObjectName("addScButton")
        self.verticalLayout_3.addWidget(self.addScButton)
        self.chkScButton = QtGui.QPushButton(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkScButton.sizePolicy().hasHeightForWidth())
        self.chkScButton.setSizePolicy(sizePolicy)
        self.chkScButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.chkScButton.setObjectName("chkScButton")
        self.verticalLayout_3.addWidget(self.chkScButton)
        self.defPrButton = QtGui.QPushButton(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defPrButton.sizePolicy().hasHeightForWidth())
        self.defPrButton.setSizePolicy(sizePolicy)
        self.defPrButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.defPrButton.setObjectName("defPrButton")
        self.verticalLayout_3.addWidget(self.defPrButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_7)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uniformRadio = QtGui.QRadioButton(self.groupBox_2)
        self.uniformRadio.setChecked(True)
        self.uniformRadio.setObjectName("uniformRadio")
        self.verticalLayout_5.addWidget(self.uniformRadio)
        self.otherRadio = QtGui.QRadioButton(self.groupBox_2)
        self.otherRadio.setChecked(False)
        self.otherRadio.setObjectName("otherRadio")
        self.verticalLayout_5.addWidget(self.otherRadio)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.repScroll = QtGui.QScrollArea(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repScroll.sizePolicy().hasHeightForWidth())
        self.repScroll.setSizePolicy(sizePolicy)
        self.repScroll.setMinimumSize(QtCore.QSize(0, 95))
        self.repScroll.setMaximumSize(QtCore.QSize(16777215, 100))
        self.repScroll.setWidgetResizable(True)
        self.repScroll.setObjectName("repScroll")
        self.repScrollContent = QtGui.QWidget(self.repScroll)
        self.repScrollContent.setGeometry(QtCore.QRect(0, 0, 761, 91))
        self.repScrollContent.setObjectName("repScrollContent")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.repScrollContent)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.repScroll.setWidget(self.repScrollContent)
        self.horizontalLayout_4.addWidget(self.repScroll)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_3 = QtGui.QScrollArea(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QtCore.QSize(0, 100))
        self.scrollArea_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget(self.scrollArea_3)
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 933, 102))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox_6)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_3)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.addScButton.setText(QtGui.QApplication.translate("MainWindow", "Add scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.chkScButton.setText(QtGui.QApplication.translate("MainWindow", "Check scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.defPrButton.setText(QtGui.QApplication.translate("MainWindow", "Define priors", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.uniformRadio.setText(QtGui.QApplication.translate("MainWindow", "Uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.otherRadio.setText(QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Conditions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "cond1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "Draw parameters values until conditions are fulfilled", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("MainWindow", "Draw parameters values only once. Discard if any condition is not fulfilled", None, QtGui.QApplication.UnicodeUTF8))

