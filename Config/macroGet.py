"""
    This file contains all functions to get values of macros.
        IMPORTS:
            configparser.ConfigParser\
        FUNCTIONS:
            generateConfig()
            getFast()
            getLayer()
            getArgon()
            getPrinting()
            getRetract()
            getWarming()
            getOuter()
            getInner()
            getFill()
            getMachiningHeight()
"""

from configparser import ConfigParser


def generateConfig():
    """
        Name: generateConfig()
            Generates a config object
        :return: config: a populated config object
    """

    config = ConfigParser()
    config.read(".\Config\config.ini")
    return config


def getFast():
    """
        Name: getFast()
            This function gets and returns the value of the fast move macro
        :return: fast: the fast wait time
    """

    config = generateConfig()
    fast = config.get('waits', 'fastWait')
    return fast


def getLayer():
    """
        Name: getLayer()
            This function gets and returns the value of the layer move macro
        :return: layer: the layer wait time
    """

    config = generateConfig()
    layer = config.get('waits', 'layerWait')
    return layer


def getArgon():
    """
        Name: getArgon()
            This function gets and returns the values of the argon macro
        :return: high/low: the high/low argon macro
    """

    config = generateConfig()
    high = config.get('macros', 'argonHigh')
    low = config.get('macros', 'argonLow')
    return high, low


def getChiller():
    """
        Name: getArgon()
            This function gets and returns the values of the argon macro
        :return: high/low: the high/low argon macro
    """

    config = generateConfig()
    high = config.get('macros', 'chillerHigh')
    low = config.get('macros', 'chillerLow')
    return high, low


def getPrinting():
    """
        Name: getPrinting()
            This function gets and returns the values of the printing macro
        :return: high/low: the high/low printing macro
    """

    config = generateConfig()
    high = config.get('macros', 'laserhighprinting')
    low = config.get('macros', 'laserlowprinting')
    return high, low


def getRetract():
    """
        Name: getRetract()
            This function gets and returns the values of the retract macro
        :return: high/low: the high/low retract macro
    """

    config = generateConfig()
    high = config.get('macros', 'retracthigh')
    low = config.get('macros', 'retractlow')
    return high, low


def getWarming():
    """
        Name: getWarming()
            This function gets and returns the values of the warming retract
        :return: high/low: the high/low retract macro
    """

    config = generateConfig()
    high = config.get('macros', 'laserhighwarming')
    low = config.get('macros', 'laserlowwarming')
    return high, low


def getOuter():
    """
        Name: getOuter()
            This function gets and returns the values of the outer macro
        :return: high/low: the high/low outer macro
    """

    config = generateConfig()
    high = config.get('macros', 'outerWallHigh')
    low = config.get('macros', 'outerWallLow')
    return high, low


def getInner():
    """
        Name: getInner()
            This function gets and returns the values of the inner macro
        :return: high/low: the high/low inner macro
    """

    config = generateConfig()
    high = config.get('macros', 'innerWallHigh')
    low = config.get('macros', 'innerWallLow')
    return high, low


def getFill():
    """
        Name: getFill()
            This function gets and returns the values of the fill macro
        :return: high/low: the high/low fill macro
    """

    config = generateConfig()
    high = config.get('macros', 'fillHigh')
    low = config.get('macros', 'fillLow')
    return high, low


def getMachiningHeight():
    """
        Name: getMachiningHeight()
            This function gets and return the values of the machining height macro
        :return: value: the value of the machining height
    """
    config = generateConfig()
    value = config.get('operation', 'machiningHeight')
    return value
