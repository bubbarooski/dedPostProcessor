"""
    This file is ran as an initial check before any user input is asked. It verifies that the
    config file exists and if it does not, then it creates one.
        IMPORTS:
            os
        FUNCTIONS:
            configFileCheck()
"""

import os


def configFileCheck():
    """
        Name: configFileCheck()
            This function is used to check if the config.ini file exists. If it does not, it
            creates a new one with base values.
    """

    fileExists = os.path.isfile(".\Config\config.ini")

    # NOTE: if new macro is added to this config list, it also needs to be added to the parser
    if not fileExists:
        file = open(".\Config\config.ini", 'a')
        file.write("[macros]\n")

        # Macro 1
        file.write("argonHigh = M101\n")
        file.write("argonLow = M201\n")

        # Argon Macro
        file.write("chillerHigh = M26\n")
        file.write("chillerLow = M27\n")

        # Macro 2
        file.write("laserHighPrinting = M102\n")
        file.write("laserLowPrinting = M202\n")

        # Macro 3
        file.write("macro3High = M103\n")
        file.write("macro3Low = M203\n")

        # Macro 4
        file.write("retractHigh = M104\n")
        file.write("retractLow = M204\n")

        # Macro 5
        file.write("laserHighWarming = M103\n")
        file.write("laserLowWarming = M203\n")

        # Macro 6
        file.write("macro6High = M106\n")
        file.write("macro6Low = M206\n")

        # Macro 7
        file.write("macro7High = M107\n")
        file.write("macro7Low = M207\n")

        # Macro 8
        file.write("macro8High = M108\n")
        file.write("macro8Low = M208\n")

        # Outer wall macro
        file.write("outerWallHigh = none\n")
        file.write("outerWallLow = none\n")

        # Inner wall Macro
        file.write("innerWallHigh = none\n")
        file.write("innerWallLow = none\n")

        # Fill Macro
        file.write("fillHigh = none\n")
        file.write("fillLow = none\n")

        file.write('\n')
        file.write('[waits]\n')

        # Fast wait
        file.write("fastWait = 2\n")

        # Layer wait
        file.write("layerWait = 60\n")

        file.write('\n')
        file.write('[operation]\n')
        file.write("machiningHeight = 1000\n")
