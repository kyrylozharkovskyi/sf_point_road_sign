# -*- coding: utf-8 -*-

"""
/***************************************************************************
  Type_preview_Dialog.py

  Type preview Dialog.
  --------------------------------------
  QGIS plugin that adds a point road sign to a traffic management design.
  Copyright: SmartFactor 2022
/***************************************************************************
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as published
 * by the Free Software Foundation.
 *
 ***************************************************************************/
"""

SCRIPT_TITLE = 'Smart Factor Road sign'
GENERAL_INFO = u"""
Wtyczka do ewidencji oznakowania pionowego

© Smart Factor 2022
library GitHub Add_a_point_road_sign is used
license: GPL v. 2
"""

# this file version: 0.1.b

import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg, uic
import subprocess

import os, math
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg, uic
from PyQt5.QtGui import QTextCursor
from qgis.core import *
from qgis.utils import iface

import pathlib


#====================================================================================================================

class Type_preview_Dialog(QtWidgets.QDialog):

    def __init__(self, parent, path):
        super(Type_preview_Dialog, self).__init__()
        self.parent = parent
        uic.loadUi(os.path.join(self.parent.base_path, 'ui', 'Type_preview_Dialog.ui'), self)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowIcon(self.parent.icon)
        #if self.parent.SVG_radioButton.isChecked():
        self.Selected_type_QSvgWidget = QtSvg.QSvgWidget(self)
        
        self.Selected_type_QSvgWidget.load(path)
        self._resize_Selected_type_QSvgWidget()
        self.pathToIS.setText(self.parent.inkScape_path)
        #QgsMessageLog.logMessage(self.parent.selected_type_path, 'skrypcior')
        self.editButton.clicked.connect(lambda:self.clickMethod(self.parent.selected_type_path))
        self.inkscapePathButton.clicked.connect(self.changeISPath)
        
        '''
        else:
            self.Selected_type_QLabel = QtWidgets.QLabel(self)
            self.raw_image = QtGui.QImage(path)
            self._resize_Selected_type_QLabel()
        '''
        self.show()

    def clickMethod(self, filePath):
        #os.system('"C:\\Program Files\\Inkscape\\bin\\inkscape" C:\\Users\\Smart\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\SF_Ewidencja_drog\\python\\plugins\\sf_point_road_sign\\img\\set_folder.svg')
        
        if(os.path.isfile(self.parent.inkScape_path + '\\inkscape.exe')):
            cmd = self.parent.inkScape_path + '\\inkscape ' + filePath
            cmd = cmd.replace("Program Files", "PROGRA~1")
            QgsMessageLog.logMessage(cmd, 'skrypcior')
            p = subprocess.Popen(cmd, shell=True)
        else:
            iface.messageBar().pushMessage("Error", "Błędna ścieżka InkScape (Folder z plikiem Inkscape.exe)", level=Qgis.Critical)

    def resizeEvent(self, event):       # overriding the method
        QtWidgets.QDialog.resizeEvent(self, event)
        #if self.parent.SVG_radioButton.isChecked():
        self._resize_Selected_type_QSvgWidget()
        #else:
        #    self._resize_Selected_type_QLabel()
    def changeISPath(self):
        _IS_path_folder = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a type groups folder:', self.parent.inkScape_path, QtWidgets.QFileDialog.ShowDirsOnly)
        defaultPathIS = os.path.join(pathlib.Path(__file__).parent.resolve(), "defaultPathIS.txt")
        f = open(defaultPathIS, "w")
        f.write(_IS_path_folder)
        f.close()
        self.parent.inkScape_path = _IS_path_folder
        self.pathToIS.setText(self.parent.inkScape_path)
        
    def _resize_Selected_type_QSvgWidget(self):
        #QgsMessageLog.logMessage(self.parent.selected_type, 'skrypcior')
        self.Selected_type_QSvgWidget.setGeometry(QtCore.QRect(0, self.editButton.height() + 20, self.width(), self.height() - self.editButton.height() - 20))
        self.setWindowTitle(self.parent.selected_type +  '       ' + str(self.width()) + ' x ' + str(self.height()))


    def _resize_Selected_type_QLabel(self):
        if self.raw_image:
            image = QtGui.QImage(self.raw_image)
            image = image.scaled(self.width(), self.height(), aspectRatioMode=QtCore.Qt.IgnoreAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.Selected_type_QLabel.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
            self.Selected_type_QLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setWindowTitle('Type preview ' + str(self.width()) + ' x ' + str(self.height()))
        

#====================================================================================================================
