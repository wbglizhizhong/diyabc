# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/setHistoricalModel.ui'
#
# Created: Tue Jan 11 13:50:26 2011
#      by: PyQt4 UI code generator 4.6
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 220))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 220))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scScroll = QtGui.QScrollArea(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scScroll.sizePolicy().hasHeightForWidth())
        self.scScroll.setSizePolicy(sizePolicy)
        self.scScroll.setMinimumSize(QtCore.QSize(500, 200))
        self.scScroll.setMaximumSize(QtCore.QSize(16777215, 200))
        self.scScroll.setWidgetResizable(True)
        self.scScroll.setObjectName("scScroll")
        self.scScrollContent = QtGui.QWidget(self.scScroll)
        self.scScrollContent.setGeometry(QtCore.QRect(0, 0, 813, 198))
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
        self.repScrollContent.setGeometry(QtCore.QRect(0, 0, 742, 93))
        self.repScrollContent.setObjectName("repScrollContent")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.repScrollContent)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.repScroll.setWidget(self.repScrollContent)
        self.horizontalLayout_4.addWidget(self.repScroll)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox_11.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_2 = QtGui.QLabel(self.groupBox_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.horizontalLayout_14.addWidget(self.groupBox_11)
        self.groupBox_12 = QtGui.QGroupBox(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        self.groupBox_12.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_12.setMaximumSize(QtCore.QSize(290, 16777215))
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtGui.QLabel(self.groupBox_12)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox_12)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox_12)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox_12)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_14.addWidget(self.groupBox_12)
        self.groupBox_13 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtGui.QLabel(self.groupBox_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.groupBox_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.groupBox_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(80, 0))
        self.label_10.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.groupBox_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(80, 0))
        self.label_11.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.horizontalLayout_14.addWidget(self.groupBox_13)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 120))
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QtCore.QSize(140, 50))
        self.groupBox_9.setMaximumSize(QtCore.QSize(140, 50))
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.paramNameLabel = QtGui.QLabel(self.groupBox_9)
        self.paramNameLabel.setObjectName("paramNameLabel")
        self.horizontalLayout_8.addWidget(self.paramNameLabel)
        self.setCondButton = QtGui.QPushButton(self.groupBox_9)
        self.setCondButton.setObjectName("setCondButton")
        self.horizontalLayout_8.addWidget(self.setCondButton)
        self.horizontalLayout_13.addWidget(self.groupBox_9)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMinimumSize(QtCore.QSize(290, 50))
        self.groupBox_10.setMaximumSize(QtCore.QSize(290, 50))
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.uniformParamRadio = QtGui.QRadioButton(self.groupBox_10)
        self.uniformParamRadio.setChecked(True)
        self.uniformParamRadio.setObjectName("uniformParamRadio")
        self.horizontalLayout_9.addWidget(self.uniformParamRadio)
        self.logUniformRadio = QtGui.QRadioButton(self.groupBox_10)
        self.logUniformRadio.setObjectName("logUniformRadio")
        self.horizontalLayout_9.addWidget(self.logUniformRadio)
        self.normalRadio = QtGui.QRadioButton(self.groupBox_10)
        self.normalRadio.setObjectName("normalRadio")
        self.horizontalLayout_9.addWidget(self.normalRadio)
        self.logNormalRadio = QtGui.QRadioButton(self.groupBox_10)
        self.logNormalRadio.setObjectName("logNormalRadio")
        self.horizontalLayout_9.addWidget(self.logNormalRadio)
        self.horizontalLayout_13.addWidget(self.groupBox_10)
        self.groupBox_14 = QtGui.QGroupBox(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy)
        self.groupBox_14.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_14)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_10.addWidget(self.lineEdit_4)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_10.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_10.addWidget(self.lineEdit_2)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_14)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.lineEdit_5)
        self.horizontalLayout_13.addWidget(self.groupBox_14)
        self.verticalLayout_2.addWidget(self.groupBox_8)
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
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 931, 98))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_3)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setToolTip(QtGui.QApplication.translate("MainWindow", "(Alt+o)", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+O", None, QtGui.QApplication.UnicodeUTF8))
        self.addScButton.setToolTip(QtGui.QApplication.translate("MainWindow", "(Alt+a)", None, QtGui.QApplication.UnicodeUTF8))
        self.addScButton.setText(QtGui.QApplication.translate("MainWindow", "Add scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.addScButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.chkScButton.setText(QtGui.QApplication.translate("MainWindow", "Check scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.defPrButton.setText(QtGui.QApplication.translate("MainWindow", "Define priors", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.uniformRadio.setText(QtGui.QApplication.translate("MainWindow", "Uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.otherRadio.setText(QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Log-uniform", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Log-normal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "minimum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "maximum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "mean", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "st-deviation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "step", None, QtGui.QApplication.UnicodeUTF8))
        self.paramNameLabel.setText(QtGui.QApplication.translate("MainWindow", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.setCondButton.setText(QtGui.QApplication.translate("MainWindow", "set condition", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Conditions", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "Draw parameters values until conditions are fulfilled", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("MainWindow", "Draw parameters values only once. Discard if any condition is not fulfilled", None, QtGui.QApplication.UnicodeUTF8))

