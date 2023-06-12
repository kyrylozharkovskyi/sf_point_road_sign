# -*- coding: utf-8 -*-

def classFactory(iface):
    from .sf_point_road_sign import sf_point_road_sign
    return sf_point_road_sign(iface)

