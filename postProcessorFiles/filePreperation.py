"""
    This file contains all of the functions needed to prepare the input file
    for postprocessing. The imports, classes, and functions are listed below:
        FUNCTIONS:
            openFile()
            lineSeparation()
"""


def openFile(fileObject, mode):
    """
        Name: openFile()
            This function is used to open the file that is being processed and add
            each line to a list.
    :param fileObject: a file object that contains info related to the file being processed
    :return: lineList: a list of lines from the opened file
    """

    lineList = []

    if mode == 0:
        directory = "./Gcode/" + fileObject.filename
        print('non GUI: ' + directory)
    else:
        directory = fileObject.filename
        print('GUI: ' + directory)

    openedFile = open(directory, 'r')

    lines = openedFile.readlines()

    # Open file and add each line to a list
    counter = 0
    for line in lines:
        lineList.append(line)
        counter = counter + 1

    return lineList


def lineSeparation(lines):
    """
        Name: lineSeparation()
            This function is used to replace existing Cura comments with FANUC style
            comments and take each line and separate each segment to create
    :param lines: a list of lines
    :return: newLineList: an edited list of lines
    """

    counter = 0
    newLineList = []

    # Replace Cura comments with FANUC comments
    for line in lines:
        if line[0] == ';':
            line = line.replace(';', '(')
            position = line.rfind('\\')
            line = line[:position] + ')' + line[position:]

        splitLine = line.split(" ")

        newLineList.append(splitLine)

        counter = counter + 1

    return newLineList
