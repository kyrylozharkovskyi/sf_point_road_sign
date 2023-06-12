# -*- coding: utf-8 -*-

"""
/***************************************************************************
  Mouse_point_tool.py

  A mouse point tool.
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

# this file version: 0.4

from qgis.core import *
from qgis.gui import *


#====================================================================================================================

class Mouse_point_tool(QgsMapTool):
    
    def __init__(self, canvas, parent):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.parent = parent
        self.start_point = None

    def canvasPressEvent(self, event):
        self.start_point = self._get_QgsPointXY(event)

    def canvasMoveEvent(self, event):
        pass
    
    def canvasReleaseEvent(self, event):
        end_point = self._get_QgsPointXY(event)
        azimuth_in_degrees = self._get_azimuth_in_degrees(self.start_point, end_point)
        self._add_point(self.start_point, azimuth_in_degrees)
        self.start_point = None
        
    def activate(self):
        QgsMapTool.activate(self)
        
    def deactivate(self):
        QgsMapTool.deactivate(self)
        
    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True

    def _get_QgsPointXY(self, event):
        x = event.pos().x()
        y = event.pos().y()
        return self.canvas.getCoordinateTransform().toMapCoordinates(x, y)

    def _get_azimuth_in_degrees(self, start_QgsPointXY, end_QgsPointXY):
        try:
            res = start_QgsPointXY.azimuth(end_QgsPointXY)
        except:
            return None
        if res < 0:
            res += 360
        return res

    def _add_point(self, qgs_point_xy, angle):
        if self.parent.set_angle_mode:
            self.parent.set_angle(angle)
        else:
            QgsMessageLog.logMessage('aloo', 'skrypcior')
        '''
            QgsMessageLog.logMessage('alo', 'skrypcior')
            if self.parent.selected_type and len(self.parent.selected_type) > 0 and self.parent.pt_width and self.parent.is_float(self.parent.pt_width):
                QgsMessageLog.logMessage('alo1', 'skrypcior')
                layer = self.parent.get_active_point_layer()
                if layer:
                    layer.startEditing()
                    faetures = layer.getFeatures()
                    for feat in faetures:
                        QgsMessageLog.logMessage('alo2', 'skrypcior')
                        #feat.setAttribute('nazwa', 'd')
                        znak = self.parent.selected_type.split('-', 1)
                        feat['kategoria_znaku'] = znak[0]
                        feat['nazwa'] = self.parent.selected_type
                        layer.updateFeature(feat)
                        layer.commitChanges()
                 
                    self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['WIDTH'], self.parent.pt_width)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['HEIGHT'], self.parent.pt_height)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['START_DATE'], self.parent.start_date)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['COMMENTS'], self.parent.comments)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['STREET_NAME'], self.parent.street_name)
                    caps = layer.dataProvider().capabilities()
                    if caps & QgsVectorDataProvider.AddFeatures:
                        feat = QgsFeature(layer.fields())
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['ROAD_SIGN_TYPE'], self.parent.selected_type)
                        if self.parent.angle and self.parent.is_float(self.parent.angle):
                             self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['ANGLE'], self.parent.angle)
                        else:
                            if angle:
                                self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['ANGLE'], angle)
                            else:
                                print("_add_point ERROR: NOT angle => angle = 0")
                                self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['ANGLE'], 0)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['WIDTH'], self.parent.pt_width)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['HEIGHT'], self.parent.pt_height)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['START_DATE'], self.parent.start_date)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['COMMENTS'], self.parent.comments)
                        self._set_attribute_if_exist(feat, self.parent.setup.DB_FIELD_NAMES_MAPPING_DICT['STREET_NAME'], self.parent.street_name)
                        feat.setGeometry(QgsGeometry.fromPointXY(qgs_point_xy))
                        (res, outFeats) = layer.dataProvider().addFeatures([feat])
                        if self.parent.iface.mapCanvas().isCachingEnabled():
                            layer.triggerRepaint()
                        else:
                            self.parent.iface.mapCanvas().refresh()
                    else:
                        print("_add_point ERROR: NOT QgsVectorDataProvider.AddFeatures")
                else:
                    print("_add_point ERROR: NOT layer")
            else:
                print("_add_point ERROR: NOT type and/or pt_width")'''

    def _set_attribute_if_exist(self, qgs_feature, attribute_name, attribute_value):
        try:
            qgs_feature.setAttribute(attribute_name, attribute_value)
        except:
            print("Can't set attribute: " + attribute_name)


#====================================================================================================================

