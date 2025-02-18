"""
    This file is ran at the beginning of the program and is used to parse the config file.
        IMPORTS:
            configparser.ConfigParser
        FUNCTIONS:
            parseConfig()
"""

from configparser import ConfigParser
parameterDictionary = {}


def parseConfig():
    """
        Name: parseConfig()
            This function is used to create a dictionary of the macro's in the config file.
    :return: parameterDictionary: a dictionary with all the macros
    """

    config = ConfigParser()
    config.read(".\Config\config.ini")
    parameterDictionary['argonHigh'] = config.get('macros', 'argonHigh')
    parameterDictionary['argonLow'] = config.get('macros', 'argonLow')
    parameterDictionary['chillerHigh'] = config.get('macros', 'chillerHigh')
    parameterDictionary['chillerLow'] = config.get('macros', 'chillerLow')
    parameterDictionary['laserHighPrinting'] = config.get('macros', 'laserHighPrinting')
    parameterDictionary['laserLowPrinting'] = config.get('macros', 'laserLowPrinting')
    parameterDictionary['macro3High'] = config.get('macros', 'macro3High')
    parameterDictionary['macro3Low'] = config.get('macros', 'macro3Low')
    parameterDictionary['retractHigh'] = config.get('macros', 'retractHigh')
    parameterDictionary['retractLow'] = config.get('macros', 'retractLow')
    parameterDictionary['laserHighWarming'] = config.get('macros', 'laserHighWarming')
    parameterDictionary['laserLowWarming'] = config.get('macros', 'laserLowWarming')
    parameterDictionary['macro6High'] = config.get('macros', 'macro6High')
    parameterDictionary['macro6Low'] = config.get('macros', 'macro6Low')
    parameterDictionary['macro7High'] = config.get('macros', 'macro7High')
    parameterDictionary['macro7Low'] = config.get('macros', 'macro7Low')
    parameterDictionary['macro8High'] = config.get('macros', 'macro8High')
    parameterDictionary['macro8Low'] = config.get('macros', 'macro8Low')
    parameterDictionary['outerWallHigh'] = config.get('macros', 'outerWallHigh')
    parameterDictionary['outerWallLow'] = config.get('macros', 'outerWallLow')
    parameterDictionary['innerWallHigh'] = config.get('macros', 'innerWallHigh')
    parameterDictionary['innerWallLow'] = config.get('macros', 'innerWallLow')
    parameterDictionary['fillHigh'] = config.get('macros', 'fillHigh')
    parameterDictionary['fillLow'] = config.get('macros', 'fillLow')
    parameterDictionary['fastWait'] = config.get('waits', 'fastWait')
    parameterDictionary['layerWait'] = config.get('waits', 'layerWait')

    """
        For printing items in the dictionary
    for items in parameterDictionary.values():
        print(items)
    """

    return parameterDictionary
