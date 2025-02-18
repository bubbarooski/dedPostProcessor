"""
    This is all that's required to update the macros in the config.ini file
    from the user.
        IMPORTS:
            configParser
        FUNCTIONS:
            setFast()
            setLayer()
            setArgon()
            setPrinting()
            setRetract()
            setWarming()
            setOuter()
            setInner()
            setFill()
            setMachiningHeight()
            macroSplit()
            fileWrite()

"""

from configparser import ConfigParser

# Creating config----------------------
config = ConfigParser()
config.read(".\Config\config.ini")
# -------------------------------------


def setFast(time):
    """
        Name: setFast()
            This function is used to set the fast move wait time.
        :param time: value to update for function
    """

    config.set('waits', 'fastWait', time)
    fileWrite()


def setLayer(time):
    """
        Name: setLayer()
            This function is used to set the layer wait time.
        :param time: value to update for function
    """

    config.set('waits', 'layerWait', time)
    fileWrite()


def setArgon(value):
    """
        Name: setArgon()
             This function is used to set the argon macro.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'argonHigh', highMacro)
    config.set('macros', 'argonLow', lowMacro)
    fileWrite()


def setChiller(value):
    """
        Name: setArgon()
             This function is used to set the chiller macro.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'chillerHigh', highMacro)
    config.set('macros', 'chillerLow', lowMacro)
    fileWrite()


def setPrinting(value):
    """
        Name: setPrinting()
            This function is used to set the printing macro.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'laserhighprinting', highMacro)
    config.set('macros', 'laserlowprinting', lowMacro)
    fileWrite()


def setRetract(value):
    """
        Name: setRetract()
            This function is used to set the retract macro.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'retracthigh', highMacro)
    config.set('macros', 'retractlow', lowMacro)
    fileWrite()


def setWarming(value):
    """
        Name: setWarming()
            This function is used to set the warming macro.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'laserhighwarming', highMacro)
    config.set('macros', 'laserlowwarming', lowMacro)
    fileWrite()


def setOuter(value):
    """
        Name: setOuter()
            This function is used to set the outer macro.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'outerWallHigh', highMacro)
    config.set('macros', 'outerWallLow', lowMacro)
    fileWrite()


def setInner(value):
    """
        Name: setInner()
            This function is used to set the inner maco.
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'innerWallHigh', highMacro)
    config.set('macros', 'innerWallLow', lowMacro)
    fileWrite()


def setFill(value):
    """
        Name: setFill()
            This function is used to set the fill macro
        :param: value: the macro value to be used
    """

    highMacro, lowMacro = macroSplit(value)
    config.set('macros', 'fillHigh', highMacro)
    config.set('macros', 'fillLow', lowMacro)
    fileWrite()


def setMachiningHeight(value):
    """
        Name: setMachiningHeight()
            This function is used to set the machining height macro
        :param: value: the macro value to be used
    """

    config.set('operation', 'machiningHeight', value)
    fileWrite()


# Helper functions ------------------------------
def macroSplit(value):
    """
        Name: macroSplit()
            This function splits an input and returns the high/low macro
        :param: value: the macro number to be split
        :return: high/low: the high/low macro
    """

    macroNum = value.split(' ')[1]
    high = 'M' + "10" + macroNum
    low = 'M' + "20" + macroNum
    return high, low


def fileWrite():
    """
        Name: fileWrite()
            This function is used to write values to the config file and
            close the config file.
    """

    with open(".\Config\config.ini", 'w') as configfile:
        config.write(configfile)
    configfile.close()
    return

# -----------------------------------------------
