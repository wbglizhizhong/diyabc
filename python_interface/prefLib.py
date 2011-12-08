# -*- coding: utf-8 -*-

## @package python_interface.preferences
# @author Julien Veyssier
#
# @brief Fenêtre pour gérer les préférences personnelles

import os,sys,platform,multiprocessing
import ConfigParser
import codecs
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore
import output
import utils.cbgpUtils as utilsPack
from utils.cbgpUtils import log
from utils.configobj.configobj import *


class GenericPreferences(QFrame):
    def __init__(self,parent=None,confFilePath=None):
        super(GenericPreferences,self).__init__(parent)

        # dico indexé par le nom de la catégorie qui contient la liste des propriétés
        self.dicoCategory = {}
        # liste pour retenir l'ordre des catégories
        self.categoryList = []

        self.configFile = confFilePath
        self.config = ConfigObj(self.configFile)

        self.createWidgets()

    def createWidgets(self):

        self.ui = self
        self.ui.verticalLayout = QtGui.QVBoxLayout(self)
        self.ui.verticalLayout.setObjectName("centralVerticalLayout")
        self.ui.tabWidget = QtGui.QTabWidget(self)
        self.ui.tabWidget.setObjectName("tabWidget")
        self.ui.verticalLayout.addWidget(self.ui.tabWidget)

    def addCategory(self,catname):
        if catname in self.categoryList:
            raise Exception("Category already exists")
        else:
            self.categoryList.append(catname)
            self.dicoCategory[catname] = []

            exec("self.tab_%s = QtGui.QWidget() "%catname)
            exec("self.tab_%s.setObjectName('tab_%s')"%(catname,catname))
            exec('self.verticalLayout_%s = QtGui.QVBoxLayout(self.tab_%s) '%(catname,catname))
            exec('self.verticalLayout_%s.setObjectName("verticalLayout_%s") '%(catname,catname))
            exec('self.scrollArea_%s = QtGui.QScrollArea(self.tab_%s) '%(catname,catname))
            exec('self.scrollArea_%s.setWidgetResizable(True) '%(catname))
            exec('self.scrollArea_%s.setObjectName("scrollArea_%s") '%(catname,catname))
            exec('self.scrollAreaWidgetContents_%s = QtGui.QWidget() '%(catname))
            exec('self.scrollAreaWidgetContents_%s.setGeometry(QtCore.QRect(0, 0, 956, 589)) '%(catname))
            exec('self.scrollAreaWidgetContents_%s.setObjectName("scrollAreaWidgetContents_%s") '%(catname,catname))
            exec('self.verticalLayoutScroll_%s = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_%s) '%(catname,catname))
            exec('self.verticalLayoutScroll_%s.setObjectName("verticalLayoutScroll_%s") '%(catname,catname))

    def addPropCheck(self,catname,propname,proptext):

        self.dicoCategory[catname].append([propname,"check",proptext])

        exec('self.frame_%s_%s = QtGui.QFrame(self.scrollAreaWidgetContents_%s) '%(catname,propname,catname))
        exec('self.frame_%s_%s.setFrameShape(QtGui.QFrame.StyledPanel) '%(catname,propname))
        exec('self.frame_%s_%s.setFrameShadow(QtGui.QFrame.Raised) '%(catname,propname))
        exec('self.frame_%s_%s.setObjectName("frame_%s_%s") '%(catname,propname,catname,propname))
        exec('self.horizontalLayout_%s_%s = QtGui.QHBoxLayout(self.frame_%s_%s) '%(catname,propname,catname,propname))
        exec('self.horizontalLayout_%s_%s.setObjectName("horizontalLayout_%s_%s") '%(catname,propname,catname,propname))
        exec('self.%sCheck = QtGui.QCheckBox(self.frame_%s_%s) '%(propname,catname,propname))
        exec('self.%sCheck.setText("%s") '%(propname,proptext))
        exec('self.%sCheck.setChecked(True) '%(propname))
        exec('self.%sCheck.setObjectName("%sCheck") '%(propname))
        exec('self.horizontalLayout_%s_%s.addWidget(self.%sCheck) '%(propname,catname,propname))
        exec('self.verticalLayoutScroll_%s.addWidget(self.frame_%s_%s) '%(catname,catname,propname))

    def addPropCombo(self,catname,propname,dicoValTxt,l_ordered_val,default_value=None):

        self.dicoCategory[catname].append( [propname,"combo",dicoValTxt,l_ordered_val,default_value] )

        exec('self.frame_%s_%s = QtGui.QFrame(self.scrollAreaWidgetContents_%s)'%(catname,propname,catname))
        exec('self.frame_%s_%s.setFrameShape(QtGui.QFrame.StyledPanel)'%(catname,propname))
        exec('self.frame_%s_%s.setFrameShadow(QtGui.QFrame.Raised)'%(catname,propname))
        exec('self.frame_%s_%s.setObjectName("frame_%s_%s")'%(catname,propname,catname,propname))
        exec('self.horizontalLayout_%s_%s = QtGui.QHBoxLayout(self.frame_%s_%s)'%(catname,propname,catname,propname))
        exec('self.horizontalLayout_%s_%s.setObjectName("horizontalLayout_%s_%s")'%(catname,propname,catname,propname))
        exec('self.label_%s = QtGui.QLabel(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.label_%s.setText("Style")'%(propname))
        exec('self.label_%s.setObjectName("label_%s")'%(propname,propname))
        exec('self.horizontalLayout_%s_%s.addWidget(self.label_%s)'%(catname,propname,propname))
        exec('self.%sCombo = QtGui.QComboBox(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.%sCombo.setObjectName("%sCombo")'%(propname,propname))
        exec('self.horizontalLayout_%s_%s.addWidget(self.%sCombo)'%(catname,propname,propname))
        exec('self.verticalLayoutScroll_%s.addWidget(self.frame_%s_%s)'%(catname,catname,propname))

        for k in l_ordered_val:
            exec('self.%sCombo.addItem("%s")'%(propname,dicoValTxt[k]))
        if default_value != None:
            exec('ind = self.ui.%sCombo.findText(default_value)'%propname)
            if ind != -1:
                exec('self.%sCombo.setCurrentIndex(%s)'%(propname,ind))

    def addPropLineEdit(self,catname,propname,labelText,default_value=""):
        self.dicoCategory[catname].append( [propname, "lineEdit", labelText, default_value] )

        exec('self.frame_%s_%s = QtGui.QFrame(self.scrollAreaWidgetContents_%s)'%(catname,propname,catname))
        exec('self.frame_%s_%s.setFrameShape(QtGui.QFrame.StyledPanel)'%(catname,propname))
        exec('self.frame_%s_%s.setFrameShadow(QtGui.QFrame.Raised)'%(catname,propname))
        exec('self.frame_%s_%s.setObjectName("frame_%s_%s")'%(catname,propname,catname,propname))
        exec('self.horizontalLayout_%s = QtGui.QHBoxLayout(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.horizontalLayout_%s.setObjectName("horizontalLayout_%s")'%(propname,propname))
        exec('self.label_%s = QtGui.QLabel(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.label_%s.setText("%s")'%(propname,labelText))
        exec('self.label_%s.setObjectName("label_%s")'%(propname,propname))
        exec('self.horizontalLayout_%s.addWidget(self.label_%s)'%(propname,propname))
        exec('self.%sEdit = QtGui.QLineEdit(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.%sEdit.setMinimumSize(QtCore.QSize(60, 0))'%(propname))
        exec('self.%sEdit.setMaximumSize(QtCore.QSize(60, 16777215))'%(propname))
        exec('self.%sEdit.setText("%s")'%(propname,default_value))
        exec('self.%sEdit.setObjectName("%sEdit")'%(propname,propname))
        exec('self.horizontalLayout_%s.addWidget(self.%sEdit)'%(propname,propname))
        #spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)'%())
        #self.horizontalLayout_%s.addItem(spacerItem)'%())
        exec('self.verticalLayoutScroll_%s.addWidget(self.frame_%s_%s)'%(propname,catname,propname))

    def addPropPathEdit(self,catname,propname,labelText,default_value=""):
        self.dicoCategory[catname].append( [propname, "path", labelText, default_value] )

        exec('self.frame_%s_%s = QtGui.QFrame(self.scrollAreaWidgetContents_%s)'%(catname,propname,catname))
        exec('self.frame_%s_%s.setFrameShape(QtGui.QFrame.StyledPanel)'%(catname,propname))
        exec('self.frame_%s_%s.setFrameShadow(QtGui.QFrame.Raised)'%(catname,propname))
        exec('self.frame_%s_%s.setObjectName("frame_%s_%s")'%(catname,propname,catname,propname))
        exec('self.horizontalLayout_%s = QtGui.QHBoxLayout(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.horizontalLayout_%s.setObjectName("horizontalLayout_%s")'%(propname,propname))
        exec('self.label_%s = QtGui.QLabel(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.label_%s.setText("%s")'%(propname,labelText))
        exec('self.label_%s.setObjectName("label_%s")'%(propname,propname))
        exec('self.horizontalLayout_%s.addWidget(self.label_%s)'%(propname,propname))
        exec('self.%sBrowseButton = QtGui.QPushButton(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.%sBrowseButton.setText("browse")'%(propname))
        exec('self.%sBrowseButton.setObjectName("%sBrowseButton")'%(propname,propname))
        exec('self.horizontalLayout_%s.addWidget(self.%sBrowseButton)'%(propname,propname))
        exec('self.%sPathEdit = QtGui.QLineEdit(self.frame_%s_%s)'%(propname,catname,propname))
        exec('self.%sPathEdit.setObjectName("%sPathEdit")'%(propname,propname))
        exec('self.horizontalLayout_%s.addWidget(self.%sPathEdit)'%(propname,propname))
        exec('self.verticalLayoutScroll_%s.addWidget(self.frame_%s_%s)'%(catname,catname,propname))

        exec('QObject.connect(self.ui.%sBrowseButton,SIGNAL("clicked()"),self.browse)'%(propname))

    def browse(self):
        but = self.sender()
        ed = but.parent.findChild(QLineEdit)
        qfd = QFileDialog()
        path = str(qfd.getOpenFileName(self,"Where is %s ?"%(str(ed.objectName()).replace("PathEdit",""))))
        ed.setText(path)

    def savePreferences(self):
        for cat in self.categoryList:
            if not self.config.has_key(cat):
                self.config[cat] = {}

            for propl in self.dicoCategory[cat]:
                propname = propl[0]
                proptype = propl[1]
                if proptype == "check":
                    exec('val_to_save = str(self.%sCheck.isChecked())'%propname)
                elif proptype == "lineEdit":
                    exec('val_to_save = str(self.ui.%sEdit.text())'%propname)
                elif proptype == "path":
                    exec('val_to_save = str(self.ui.%sPathEdit.text())'%propname)
                elif proptype == "combo":
                    exec('txt = str(self.ui.%sCombo.currentText())'%propname)
                    for k in propl[2].keys():
                        a = propl[2][k]
                        if a == txt:
                            break
                    val_to_save = a

                self.config[cat][propname] = val_to_save

        
        self.writeConfigFile()

    def loadPreferences(self):
        cfg = self.config

        for cat in self.dicoCategory.keys():
            if cfg.has_key(cat):
                for propl in dicoCategory[cat].keys():
                    propname = propl[0]
                    if cfg[cat].has_key(propname):
                        val = cfg[cat][propname]
                        proptype = propl[1]
                        if proptype == "check":
                            checked = (val == "True")
                            exec('self.ui.%sCheck.setChecked(not checked)'%propname)
                            exec('self.ui.%sCheck.setChecked(checked)'%propname)
                        elif proptype == "lineEdit":
                            exec('self.ui.%sEdit.setText(str(val).strip())'%propname)
                        elif proptype == "path":
                            exec('self.ui.%sPathEdit.setText(str(val).strip())'%propname)
                        elif proptype == "combo":
                            exec('ind = self.ui.%sCombo.findText(propl[2][str(val)])'%propname)
                            if ind != -1:
                                exec('self.ui.%sCombo.setCurrentIndex(ind)'%propname)




