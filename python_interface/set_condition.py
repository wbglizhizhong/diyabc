# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from set_condition_ui import Ui_MainWindow

class SetCondition(QMainWindow):
    """ Fenetre de definition d'une condition
    """
    def __init__(self,param,target_list,parent=None):
        super(SetCondition,self).__init__(parent)
        self.parent=parent
        self.param = param
        self.target_list = target_list
        self.createWidgets()

    def createWidgets(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.paramLabel.setText(self.param)
        for t in self.target_list:
            self.ui.targetComboBox.addItem(t)
        QObject.connect(self.ui.cancelButton,SIGNAL("clicked()"),self.close)
        QObject.connect(self.ui.validateButton,SIGNAL("clicked()"),self.valid)

    def valid(self):
        """ clic sur le bouton de validation qui entraine l'affichage de la condition dans setHistoricalModel
        """
        if self.ui.infRadio.isChecked():
            op = '<'
        elif self.ui.infERadio.isChecked():
            op = '<='
        elif self.ui.supERadio.isChecked():
            op = '>='
        else:
            op = '>'
        selected_target = self.ui.targetComboBox.currentText()
        my_condition = "%s %s %s"%(self.param,op,selected_target)
        inverseur = {"<":">=",">":"<=",">=":"<","<=":">"}
        mirroir = {"<=":">=",">=":"<=",">":"<","<":">"}
        incoherent = {"<=":"<",">=":">",">":">=","<":"<="}
        # pour a > b : b < a ; cad la meme ecrite a l'envers
        my_condition_mirroir = "%s %s %s"%(my_condition.split(' ')[2],mirroir[my_condition.split(' ')[1]],my_condition.split(' ')[0])
        # pour a > b : opposée vaut a <= b
        my_condition_opposee = "%s %s %s"%(my_condition.split(' ')[0],inverseur[my_condition.split(' ')[1]],my_condition.split(' ')[2])
        # pour a > b : opp_mirroir vaut b >= a
        my_condition_mirroir_opposee = "%s %s %s"%(my_condition.split(' ')[2],mirroir[inverseur[my_condition.split(' ')[1]]],my_condition.split(' ')[0])
        # pour a > b : a < b
        my_condition_incompatible = "%s %s %s"%(my_condition.split(' ')[0],mirroir[my_condition.split(' ')[1]],my_condition.split(' ')[2])
        # pour a > b : b > a
        my_condition_incompatible_mirroir = "%s %s %s"%(my_condition.split(' ')[2],my_condition.split(' ')[1],my_condition.split(' ')[0])
        # pour a > b : a >= b
        my_condition_incoherent = "%s %s %s"%(my_condition.split(' ')[0],incoherent[my_condition.split(' ')[1]],my_condition.split(' ')[2])
        # pour a > b : b <= a
        my_condition_incoherent_mirroir = "%s %s %s"%(my_condition.split(' ')[2],mirroir[incoherent[my_condition.split(' ')[1]]],my_condition.split(' ')[0])
        for cond_box in self.parent.condList:
            econdition = str(cond_box.findChild(QLabel,"condLabel").text())
            if my_condition == econdition or econdition == my_condition_mirroir:
                QMessageBox.information(self,"Error","This condition (%s) already exists (%s)"%(my_condition,econdition))
                return 0
            elif econdition == my_condition_opposee or econdition == my_condition_mirroir_opposee:
                QMessageBox.information(self,"Error","The opposite of your new condition (%s) already exists (%s)"%(my_condition,econdition))
                return 0
            elif econdition == my_condition_incompatible or econdition == my_condition_incompatible_mirroir:
                QMessageBox.information(self,"Error","Your new condition (%s) is incompatible with an existing one (%s)"%(my_condition,econdition))
                return 0
            elif econdition == my_condition_incoherent or econdition == my_condition_incoherent_mirroir:
                QMessageBox.information(self,"Error","Your new condition (%s) is incoherent with an existing one (%s)"%(my_condition,econdition))
                return 0


        ## TODO verifier avec (self.param ; op ; selected_targer) qu'on peut ajouter la condition en utilisant self.parent.condList
        #    #utiliser findChild(QPlainTextEdit,"scplainTextEdit")

        ## construction d'un dico d[param] = [op,param] :
        #cond_dico = {}
        ## pour tous les params, dico[param] = dicovide key : op ; value : autre param
        #for param_box in self.parent.paramList:
        #    param = str(param_box.findChild(QLabel,"paramNameLabel").text())
        #    cond_dico[param] = {}
        #    cond_dico[param]['<'] = []
        #    cond_dico[param]['<='] = []
        #    cond_dico[param]['>='] = []
        #    cond_dico[param]['>'] = []

        #for cond_box in self.parent.condList:
        #    cond_txt = str(cond_box.findChild(QLabel,"condLabel").text())
        #    param1 = cond_txt.split(' ')[0]
        #    op = cond_txt.split(' ')[1]
        #    param2 = cond_txt.split(' ')[2]

        #    # dans un sens
        #    cond_dico[param1][op].append(param2)
        #    # plus sioux : dans l'autre sens
        #    if op == '<=':
        #        op = '>='
        #    elif op == '>=':
        #        op = '<='
        #    elif op == '>':
        #        op = '<'
        #    elif op == '<':
        #        op = '>'
        #    print param1+"|||"+op+"|||"+param2
        #    cond_dico[param2][op].append(param1)
        #print cond_dico


        self.parent.addCondition("%s %s %s"%(self.param,op,selected_target))
        self.close()