"""
    This file is the main driver file of the program. It calls the menu function,
    which controls the entire program.
        IMPORTS:
            Config.initialCheck
            StartUpProcesses.directoryCheck
            GUI.guiDriver
        FUNCTIONS:
            beginningProcesses()
            gui()
"""


def beginningProcesses():
    """
        Name: beginningProcesses()
            This function is used to verify if all requisite directories and files are
            in place. It also handles checking of the config file.
    """
    from Config import configCheck
    from StartUpProcesses import directoryCheck

    directoryCheck.directoryDriver()
    configCheck.configFileCheck()


def gui():
    """
        Name: gui()
            This function is used to run the gui in its entirety.
    """
    from GUI import guiDriver
    guiDriver.driver()


beginningProcesses()
gui()
