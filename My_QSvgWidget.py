# -*- coding: utf-8 -*-

"""
/***************************************************************************
  My_QSvgWidget.py

  My QSvgWidget QT5 widget with mouseReleaseEvent handled.
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

# this file version: 0.2

from PyQt5 import QtSvg

import os, math
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg, uic
from qgis.core import *
from qgis.utils import iface
import pathlib


#====================================================================================================================

class My_QSvgWidget(QtSvg.QSvgWidget):
    
    def __init__(self, parent, path):
        super(My_QSvgWidget, self).__init__()
        self.parent = parent
        self.path = path
        #QgsMessageLog.logMessage(path, 'MyPlugin')
    def mouseReleaseEvent(self, e):  
        self.parent.set_selected_type_QSvgWidget(self.path)


#====================================================================================================================
