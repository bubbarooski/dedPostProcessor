"""
    This file is used to check if these directories have been made in a proper distribution
    and use of this software. If they have not, then create those folders.
        IMPORTS:
            os
            shutil
        FUNCTIONS:
            directoryDriver()
            checkConfig()
            checkGcode()
            checkImages()
"""

import os
import shutil


def directoryDriver():
    """
        Name: directoryDriver()
            This functions simply calls the two directory check files.
    """

    checkConfig()
    checkGcode()
    checkImages()


def checkConfig():
    """
        Name: checkConfig()
            This function checks if the "Config" directory exists and if it doesn't,
            create it.
    """

    configExists = os.path.isdir('Config')

    if not configExists:
        directory = "Config"
        os.mkdir(directory)


def checkGcode():
    """
        Name: checkGcode()
            This function checks if the "Gcode" directory exists and if it doesn't,
            create it.
    """

    gcodeExists = os.path.isdir('Gcode')

    if not gcodeExists:
        directory = "Gcode"
        os.mkdir(directory)


def checkImages():
    """
            Name: checkGcode()
                This function checks if the "images" directory exists and if it doesn't,
                create it. It pulls from the images placed into the '_internal' directory
                from auto-py-to-exe.
        """

    gcodeExists = os.path.isdir('images')

    if not gcodeExists:
        directory = 'images'
        os.mkdir(directory)

        sourceDir = '.\_internal\images\\'
        destinationDir = '.\images'
        for filename in os.listdir(sourceDir):
            print(filename)
            shutil.copy(sourceDir+filename, destinationDir)
