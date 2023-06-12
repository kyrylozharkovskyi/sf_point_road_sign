# -*- coding: utf-8 -*-

"""
/***************************************************************************
  My_QLabel.py

  My QLabel QT5 widget with mouseReleaseEvent handled.
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

from PyQt5 import QtWidgets


#====================================================================================================================

class My_QLabel(QtWidgets.QLabel):
    
    def __init__(self, parent, path):
        super(My_QLabel, self).__init__()
        self.parent = parent
        self.path = path

    def mouseReleaseEvent(self, e):  
        self.parent.set_selected_type_QLabel(self.path)


#====================================================================================================================
