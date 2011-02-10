# -*- coding: utf-8 -*-

import os
import shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from comparison_ui import Ui_Frame
from genericScenarioSelection import GenericScenarioSelection

class Comparison(QFrame):
    def __init__(self,analysis,parent=None):
        super(Comparison,self).__init__(parent)
        self.parent=parent
        self.analysis = analysis
        self.scNumList = []
        self.dico_values = {}
        self.createWidgets()
        self.ui.verticalLayout_2.setAlignment(Qt.AlignHCenter)
        self.ui.verticalLayout_2.setAlignment(Qt.AlignTop)



    def createWidgets(self):
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        QObject.connect(self.ui.exitButton,SIGNAL("clicked()"),self.exit)
        QObject.connect(self.ui.okButton,SIGNAL("clicked()"),self.validate)
        QObject.connect(self.ui.redefButton,SIGNAL("clicked()"),self.redefineScenarios)


    def validate(self):
        #self.parent.parent.addRow("scenario choice","params","4","new")
        self.analysis.append(self.scNumList)
        self.majDicoValues()
        self.analysis.append(self.dico_values)
        self.parent.parent.addAnalysis(self.analysis)
        self.exit()

    def setScenarios(self,scList):
        plur= ""
        if len(scList)>1:
            plur = "s"
            
        lstxt=""
        self.scNumList = []
        for i in scList:
            lstxt+="%s, "%i
            self.scNumList.append(i)
        lstxt = lstxt[:-2]

        txt = "Chosen scenario%s : %s"%(plur,lstxt)
        self.ui.scenariosLabel.setText(txt)

    def redefineScenarios(self):
        """ repasse sur le choix des scenarios en lui redonnant moi même comme next_widget
        """
        estimateFrame = self
        genSel = GenericScenarioSelection(len(self.parent.parent.hist_model_win.scList),"Parameters will be estimated considering data sets simulated with",estimateFrame,"ABC parameter estimation",2,self.parent)
        self.parent.parent.addTab(genSel,"Scenario selection")
        self.parent.parent.removeTab(self.parent.parent.indexOf(self))
        self.parent.parent.setCurrentWidget(genSel)

    def majDicoValues(self):
        self.dico_values["chosenNumberOfselData"] = str(self.ui.cnosdEdit.text())
        self.dico_values["de"] = str(self.ui.deEdit.text())
        self.dico_values["lr"] = str(self.ui.lrEdit.text())

    def exit(self):
        # reactivation des onglets
        self.parent.parent.setTabEnabled(1,True)
        self.parent.parent.setTabEnabled(0,True)
        self.parent.parent.removeTab(self.parent.parent.indexOf(self))
        self.parent.parent.setCurrentIndex(1)
