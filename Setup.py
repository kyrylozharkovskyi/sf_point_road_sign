# -*- coding: utf-8 -*-

# this file version: 0.6

class Setup:
    
    WIDTH = 7
    HEIGHT = 7
    START_DATE = ''
    COMMENTS = ''
    STREET_NAME = ''

    COMMENTS_MAX_LENGTH = 100
    STREET_NAME_MAX_LENGTH = 100
    DB_FIELD_NAMES_MAPPING_DICT = {
        'ROAD_SIGN_TYPE': 'nazwa',
        'ANGLE': 'azimuth',
        'WIDTH': '',
        'HEIGHT': '',
        'START_DATE': 'data_wprowadzenia',
        'COMMENTS': 'uwagi_koder',
        'STREET_NAME': ''
        }
    MANUAL_FILE_NAME = 'APRS_manual_EN.pdf'
