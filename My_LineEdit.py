# -*- coding: utf-8 -*-

"""
/***************************************************************************
  My_LineEdit.py

  My QLineEdit QT5 widget with enter pressed event handled.
  --------------------------------------
  QGIS plugin displaying photos from road inspection.
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

# this file version: 0.1

from PyQt5 import QtCore, QtWidgets
import os, math
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg, uic
from PyQt5.QtGui import QTextCursor
from qgis.core import *
from qgis.utils import iface
from .Setup import Setup
from .Mouse_point_tool import Mouse_point_tool
from .My_QSvgWidget import My_QSvgWidget
from .My_QLabel import My_QLabel
from .Type_preview_Dialog import Type_preview_Dialog

#====================================================================================================================

class My_LineEdit(QtWidgets.QLineEdit):

    enter_pressed_signal = QtCore.pyqtSignal()
    
    def __init__(self, *args):
        super(My_LineEdit, self).__init__(*args)
        
    def event(self, event):
        if (event.type() == QtCore.QEvent.KeyPress):# and (event.key() == QtCore.Qt.Key_Enter):
            
            #return True
            try:
                return QtWidgets.QLineEdit.event(self, event)
            finally:
                self.enter_pressed_signal.emit()
        return QtWidgets.QLineEdit.event(self, event)
#====================================================================================================================
