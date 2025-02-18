"""
    This file contains the classes and functions needed to post process the input
    file. The imports, classes, and functions are listed below:
        IMPORTS:
            collections
            postProcessorFiles.filePreperation
            Config.parse.parseConfig
            Config.macroGet import getMachiningHeight
            postProcessorFiles.postProcessorHelperFunctions.macroReplacement
        CLASSES:
            file
            codes
        FUNCTIONS
            postProcessingControlFunction()
                addLineNumbers()
                removeCura()
                smallChanges()
                warmingLayer()
                printingCodes()
                removeAndReplace()
                comments()
                writeNewFile()
"""

import collections
import postProcessorFiles.filePreperation as filePreperation
from Config.parse import parseConfig as parseConfig
from Config.macroGet import getMachiningHeight, getLayer, getFast
from postProcessorFiles.postProcessorHelperFunctions import macroReplacement, coordinateList
import postProcessorFiles.postProcessTests as ppTests


# PERTINENT CLASSES
# -----------------------------------------------
class file:
    """
        Name: file
            This class is used to store variables related to the file being processed
            including the imported file name, the FANUC file number, and the exported
            file name.
    """

    def __init__(self, filename, fileNumber, exportFilename, layerWait, fastWait):
        self.filename = filename
        self.fileNumber = fileNumber
        self.exportFilename = exportFilename
        self.layerWait = getLayer()
        self.fastWait = getFast()

        global warmedEnd, warmedStart, noLayers
        warmedEnd = 0
        warmedStart = 0
        noLayers = ""
# -----------------------------------------------


# -----------------------------------------------
class codes:
    """
        Name: codes
            This class is used to store all M codes used during the post-processing
            passes
    """

    def __init__(self):
        macroDictionary = parseConfig()

        # Macro 1
        self.argonHigh = macroDictionary.get('argonHigh')
        self.argonLow = macroDictionary.get('argonLow')

        # Chiller
        self.chillerHigh = macroDictionary.get('chillerHigh')
        self.chillerLow = macroDictionary.get('chillerLow')

        # Macro 2
        self.laserHighPrinting = macroDictionary.get('laserHighPrinting')
        self.laserLowPrinting = macroDictionary.get('laserLowPrinting')

        # Macro 3
        self.macro3High = macroDictionary.get('macro3High')
        self.macro3Low = macroDictionary.get('macro3Low')

        # Macro 4
        self.retractHigh = macroDictionary.get('retractHigh')
        self.retractLow = macroDictionary.get('retractLow')

        # Macro 5
        self.laserHighWarming = macroDictionary.get('laserHighWarming')
        self.laserLowWarming = macroDictionary.get('laserLowWarming')

        # Macro 6
        self.macro6High = macroDictionary.get('macro6High')
        self.macro6Low = macroDictionary.get('macro6Low')

        # Macro 7
        self.macro7High = macroDictionary.get('macro7High')
        self.macro7Low = macroDictionary.get('macro7Low')

        # Macro 8
        self.macro8High = macroDictionary.get('macro8High')
        self.macro8Low = macroDictionary.get('macro8Low')

        self.outerWallHigh = macroDictionary.get('outerWallHigh')
        self.outerWallLow = macroDictionary.get('outerWallLow')

        self.innerWallHigh = macroDictionary.get('innerWallHigh')
        self.innerWallLow = macroDictionary.get('innerWallLow')

        self.fillHigh = macroDictionary.get('fillHigh')
        self.fillLow = macroDictionary.get('fillLow')

# -----------------------------------------------


# -----------------------------------------------------------------------------
def postProcessingControlFunction(fileObject, mode):
    """
        Name: postProcessingControlFunction()
            This function is used to control the flow of post-processing. It creates
            pertinent objects, creates the list of lines, and calls each pass of the
            post processor.
    :param fileObject: an object file with variables relating to the input and output file
    :param mode: decides if function is a full process or showing changes
    """

    print('--START OF POST PROCESSING--')

    # Creation of objects
    mainFile = fileObject
    codesList = codes()

    # Creation of lines
    mainFile.fileLines = filePreperation.openFile(mainFile, mode)
    mainFile.fileLines = filePreperation.lineSeparation(mainFile.fileLines)

    # Processing of file ----------------------------------
    print('PASS 1')
    mainFile.fileLines = addLineNumbers(mainFile.fileLines)

    print('PASS 2')
    mainFile.fileLines = removeCura(mainFile.fileLines, codesList)

    print('PASS 3')
    mainFile.fileLines = smallChanges(mainFile)

    print('PASS 4')
    mainFile.fileLines = warmingLayer(mainFile.fileLines, codesList, mainFile)

    print('PASS 5')
    mainFile.fileLines = printingCodes(mainFile.fileLines, codesList, fileObject)

    print('PASS 6')
    mainFile.fileLines = removeAndReplace(mainFile.fileLines, fileObject, codesList)

    print('PASS 7')
    mainFile.fileLines = comments(mainFile.fileLines, mainFile, codesList)

    print('PASS 8')
    if mode == 0:
        ppTests.test(mainFile.fileLines, codesList)
        writeNewFile(mainFile)
    else:
        return mainFile.fileLines
    # -----------------------------------------------------

    # testPrinting(mainFile.fileLines)
# -----------------------------------------------------------------------------


# PASS 1 ----------------------------------------
def addLineNumbers(fileLines):
    """
        Name: addLineNumbers() - PASS 1
            This function adds line #'s to each line. Cura doesn't natively
            generate line #'s but FANUC needs them.
    :param fileLines: a list of file lines
    :return: newLines: a new list of lines with line #'s added
    """

    newLines = []

    # FANUC line numbers increase by 10
    counter = int(10)

    # For each line, create a deque to allow for insertion of line number
    for line in fileLines:
        lineNumber = 'N' + str(counter)
        lineDeque = collections.deque(line)
        lineDeque.insert(0, lineNumber)
        newList = list(lineDeque)

        newLines.append(newList)

        counter = counter + 10

    return newLines
# -----------------------------------------------


# PASS 2 ----------------------------------------
def removeCura(fileLines, codesList):
    """
            Name: removeCodesAndComments() - PASS 2
                This function is used to remove certain codes and comments that
                Cura natively generates.
        :param fileLines: a list of file lines
        :param codesList: a list of Meltio specific M codes
        :return: newLines: a new list of lines with changes done to them
        """
    newLines = []

    # Removing unnecessary lines generated by Cura
    counter = 0
    for line in fileLines:
        # Remove setting lines
        if "SETTING_3" in line[1]:
            counter += 1
            continue

        # Remove M104 code
        if codesList.retractHigh in line[1]:
            counter += 1
            continue

        # Remove M204 code
        if codesList.retractLow in line[1]:
            counter += 1
            continue

        # Remove M109 code
        if "M109" in line[1]:
            counter += 1
            continue

        # Remove M82 code
        if "M82" in line[1]:
            counter += 1
            continue

        # Remove G92 code
        if "G92" in line[1]:
            counter += 1
            continue

        # Remove M107 code
        if "M107" in line[1]:
            counter += 1
            continue

        # Remove TIME_ELAPSED comment
        if "TIME_ELAPSED" in line[1]:
            counter += 1
            continue

        """
        # Remove total time elapsed comment
        if "(TIME" in line[1]:
            counter += 1
            continue
        """

        # Remove MESH comments
        if "MESH" in line[1]:
            counter += 1
            continue

        counter += 1
        newLines.append(line)

    # Removal of cura "END OF GCODE" comment
    newLines = newLines[:-1]
    return newLines
# -----------------------------------------------


# PASS 3 ----------------------------------------
def smallChanges(fileObject):
    """
        Name: smallChanges() - PASS 3
            This functions is used to make small changes to the file before the
            bulk of the post-processing begins.
    :param fileObject: an object file with variables relating to the input and output file
    :return: newLines: a new list of lines with changes done to them
    """
    newLines = []

    for line in fileObject.fileLines:
        # Change G0 to G1
        if line[1] == 'G0':
            line[1] = 'G1'

        # Finding print layer height
        if 'MINZ' in line[1]:
            string = line[1].split(':')[1]
            layerHeight = string.split(')')[0]
            fileObject.layerHeight = layerHeight

        if line[1] == 'M101':
            newLines.append(['NX', 'M26', '(CHILLER ON)'])

        if line[1] == 'M201':
            newLines.append(['NX', 'M27', '(CHILLER OFF)'])

        # Changing all segments to upper case and remove new line characters
        tempList = []
        for segment in line:
            # Make all characters upper case
            newSegment = segment.upper()

            # Removal of new line character
            newSegment = newSegment.strip()

            tempList.append(newSegment)

        # Replacing the original line with the newly changed line
        line = tempList

        newLines.append(line)

    # Replace all non F600 with F600
    counter = 0
    while counter < len(newLines):
        try:
            if newLines[counter][2][0] == 'F':
                if newLines[counter][2] == 'F3600':
                    pass
                else:
                    if newLines[counter][2] == 'F600':
                        pass
                    else:
                        newLines[counter][2] = 'F600'
            counter += 1
        except:
            counter += 1

    return newLines
# -----------------------------------------------


# PASS 4 ----------------------------------------
def warmingLayer(fileLines, codesList, fileObject):
    """
        Name: warmingLayer() - PASS 4
            This function is used to insert the warming layer into the new code. This
            layer is a copy of the first layer with a different laser on/off M code.
    :param fileLines: a list of file lines
    :param codesList: a list of Meltio specific M codes
    :param fileObject: an object file with variables relating to the input and output file
    :return: newLines: a new list of lines with changes done to them
    """
    newLines = []
    fileObject.warmedStart = 0
    fileObject.warmedEnd = 0
    counter = 0

    # Finding start/end line #'s of warming layer
    for line in fileLines:
        if "(LAYER:0)" in line:
            fileObject.warmedStart = counter
            # print(warmedStart)
        if "(LAYER:1)" in line:
            fileObject.warmedEnd = counter
            # print(warmedEnd)
        counter += 1

        if fileObject.warmedEnd != 0:
            break

    # Adding warming layer, including warming laser and ending retract
    counter = 0
    while counter < fileObject.warmedEnd:
        if "(LAYER:0)" in fileLines[counter]:
            counter += 1
            newLines.append(['NX', '(WARM PLATE)'])
            newLines.append(['NX', '(-----------)'])
            newLines.append(fileLines[counter])
            counter += 1
            newLines.append(['NX', codesList.laserHighWarming, '(LASER HIGH)'])

        newLines.append(fileLines[counter])
        counter += 1

    newLines.append(['NX', codesList.laserLowWarming, '(LASER LOW)'])
    counter += 1

    # Add rest of code after warming layer
    counter = fileObject.warmedStart
    while counter < len(fileLines):
        newLines.append(fileLines[counter])
        counter += 1

    # Determine where normal layers begin for future passes
    counter = 0
    for lines in newLines:
        if "(LAYER:0)" in lines:
            fileObject.warmedEnd = counter
            break
        counter += 1

    return newLines
# -----------------------------------------------


# PASS 5 ----------------------------------------
def printingCodes(fileLines, codesList, fileObject):
    """
        Name: printingCodes()
            This function is used to input the specific codes for Meltio
            and FANUC to cooperate together. This is the bulk of the post-processing.
    :param fileLines: a list of file lines
    :param codesList: a list of Meltio specific M codes
    :param fileObject: an object file with variables relating to the input and output file
    :return: newLines: a new list of lines with changes done to them
    """

    newLines = []
    counter = int(fileObject.warmedEnd)
    fileObject.layerCount = 0
    currentLayer = None
    skip = False
    option = False

    # Determine total layer count of program
    while counter < len(fileLines):
        # Determining number of layers
        if '(LAYER' in fileLines[counter][1]:
            fileObject.layerCount += 1
        counter += 1

    counter = int(fileObject.warmedEnd)

    # Main loop for adding codes - while loop needed because of list manipulation
    while counter < len(fileLines):

        # Determine what layer we are on
        if "(LAYER" in fileLines[counter][1]:
            temp = fileLines[counter][1].split(':')[1]
            currentLayer = temp.split(')')[0]

        # Fast move retract and wait
        try:
            # Testing for fast move at end of layer
            if fileLines[counter][2] == 'F3600':
                tempCounter = counter
                for i in range(1, 3):
                    if "(LAYER:" in fileLines[tempCounter + i][1]:
                        if "F3600" in fileLines[tempCounter + i - 1][2]:
                            if fileLines[tempCounter + i - 2][4][1] == 'Z':
                                pass
                        skip = True
                    else:
                        pass
        except:
            pass

        # Adding lines if not at end of layer
        if skip:
            pass
        # (this is now the most disgusting chunk of code ive ever written)
        else:
            tempCounter = counter

            # Adding lines at wall change within layer
            if 'F3600' in fileLines[tempCounter] and "(TYPE" in fileLines[tempCounter + 1][1] or \
                    'F3600' in fileLines[tempCounter] and "(TYPE" in fileLines[tempCounter + 2][1]:
                while True:
                    try:
                        if 'A' in fileLines[tempCounter][4] or 'A' in fileLines[tempCounter][5]:
                            if 'F3600' in fileLines[tempCounter + 1]:
                                fileLines.insert(tempCounter + 1, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                   '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                fileLines.insert(tempCounter + 1, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                fileLines.insert(tempCounter + 1, ['NX', codesList.retractHigh, '(RETRACT HIGH)'])
                                tempCounter += 3
                                counter += 3

                                while True:
                                    if '(TYPE' in fileLines[tempCounter][1]:
                                        fileLines.insert(tempCounter + 1,
                                                         ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                        tempCounter += 1
                                        counter += 1
                                        fileLines[tempCounter + 1].append(codesList.laserLowPrinting)
                                        fileLines[tempCounter + 1].append('(LASER LOW)')
                                        # fileLines[tempCounter + 1].append('(wall change, c1)')

                                        break
                                    else:
                                        tempCounter += 1
                                break
                            else:
                                skip = False
                                for x in range(0,6):
                                    if "(LAYER" in fileLines[tempCounter-x][1]:
                                        skip = True
                                if skip:
                                    break
                                fileLines[tempCounter+1].append(codesList.retractHigh)
                                fileLines[tempCounter + 1].append('(RETRACT HIGH)')
                                if 'F3600' in fileLines[tempCounter+2]:
                                    fileLines.insert(tempCounter + 2, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                       '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                    fileLines.insert(tempCounter + 2, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                    counter += 2
                                    tempCounter += 2

                                    while True:
                                        if '(TYPE' in fileLines[tempCounter][1]:
                                            fileLines.insert(tempCounter + 1, ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                            counter += 1
                                            fileLines[tempCounter + 2].append(codesList.laserLowPrinting)
                                            fileLines[tempCounter + 2].append('(LASER LOW)')
                                            # fileLines[tempCounter + 2].append('(wall change, c2)')
                                            break
                                        else:
                                            tempCounter += 1
                                    break
                                else:
                                    fileLines[tempCounter + 2].append(codesList.retractLow)
                                    fileLines[tempCounter + 2].append('(RETRACT LOW)')
                                    fileLines.insert(tempCounter + 3, ['NX', 'G04', 'P' + fileObject.fastWait,
                                                                       '(WAIT ' + fileObject.fastWait + ' MILLISECONDS)'])
                                    counter += 1
                                    while True:
                                        if '(TYPE' in fileLines[tempCounter][1]:
                                            fileLines.insert(tempCounter + 1, ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                            counter += 1
                                            fileLines[tempCounter + 2].append(codesList.laserLowPrinting)
                                            fileLines[tempCounter + 2].append('(LASER LOW)')
                                            # fileLines[tempCounter + 2].append('(wall change, c2)')
                                            break
                                        else:
                                            tempCounter += 1
                                    break
                        else:
                            tempCounter -= 1
                    except:
                        tempCounter -= 1

            # Adding lines for rest of F3600 moves
            tempCounter = counter
            if 'F3600' in fileLines[tempCounter] and "(TYPE" not in fileLines[tempCounter + 1][1] or \
                    'F3600' in fileLines[tempCounter] and "(TYPE" not in fileLines[tempCounter + 2][1]:
                while True:
                    try:
                        if 'A' in fileLines[tempCounter][4] or 'A' in fileLines[tempCounter][5]:
                            if 'F3600' in fileLines[tempCounter + 1]:
                                fileLines.insert(tempCounter + 1, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                   '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                fileLines.insert(tempCounter + 1, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                fileLines.insert(tempCounter + 1, ['NX', codesList.retractHigh, '(RETRACT HIGH)'])
                                tempCounter += 3
                                counter += 3
                                otherTempCounter = tempCounter
                                while True:
                                    if fileLines[otherTempCounter][2] == 'F600':
                                        fileLines.insert(otherTempCounter,
                                                         ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                        counter += 1
                                        fileLines[otherTempCounter + 1].append(codesList.laserLowPrinting)
                                        fileLines[otherTempCounter + 1].append('(LASER LOW)')
                                        # fileLines[otherTempCounter].append('(fast move, c1)')
                                        break
                                    else:
                                        otherTempCounter += 1
                                break
                            else:
                                skip = False
                                for x in range(0, 10):
                                    if "(LAYER" in fileLines[tempCounter + x][1]:
                                        # print(fileLines[tempCounter + x])
                                        skip = True
                                for x in range(0, 5):
                                    if "(LAYER" in fileLines[tempCounter - x][1]:
                                        # print(fileLines[tempCounter - x])
                                        skip = True
                                for x in range(0,5):
                                    if "(TYPE" in fileLines[tempCounter + x][1]:
                                        # print(fileLines[tempCounter + x])
                                        skip = True
                                for x in range(0, 3):
                                    if "(TYPE" in fileLines[tempCounter - x][1]:
                                        # print(fileLines[tempCounter + x])
                                        skip = True
                                for x in range(0, 3):
                                    if "F3600" in fileLines[tempCounter + x][2]:
                                        # print(fileLines[tempCounter + x])
                                        skip = False
                                if skip:
                                    break

                                fileLines[tempCounter+1].append(codesList.retractHigh)
                                fileLines[tempCounter + 1].append('(RETRACT HIGH)')
                                # fileLines[tempCounter + 1].append('(find)')
                                if 'F3600' in fileLines[tempCounter+2]:
                                    fileLines.insert(tempCounter + 2, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                       '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                    fileLines.insert(tempCounter + 2, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                    tempCounter += 2
                                    counter += 2
                                    otherTempCounter = tempCounter
                                    while True:
                                        if fileLines[otherTempCounter][2] == 'F600':
                                            fileLines.insert(otherTempCounter, ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                            counter += 1
                                            fileLines[otherTempCounter + 1].append(codesList.laserLowPrinting)
                                            fileLines[otherTempCounter + 1].append('(LASER LOW)')
                                            # fileLines[otherTempCounter].append('(fast move, c2)')
                                            option = True
                                            break
                                        else:
                                            otherTempCounter += 1
                                    if option:
                                        break
                                    else:
                                        otherTempCounter = tempCounter
                                        while True:
                                            if 'F600' in fileLines[otherTempCounter]:
                                                fileLines.insert(otherTempCounter, ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                                fileLines[otherTempCounter + 1].append(codesList.laserLowPrinting)
                                                fileLines[otherTempCounter + 1].append('(LASER LOW)')
                                                # fileLines[otherTempCounter + 1].append('(fast move, c2)')
                                                break
                                            else:
                                                otherTempCounter += 1
                                        break
                                else:
                                    fileLines[tempCounter + 2].append(codesList.retractLow)
                                    fileLines[tempCounter + 2].append('(RETRACT LOW)')
                                    # fileLines[tempCounter + 2].append('(test)')
                                    newCounter = tempCounter
                                    while True:
                                        if newCounter > tempCounter + 5:
                                            break
                                        elif 'F3600' in fileLines[newCounter + 3]:
                                            fileLines.insert(newCounter + 3, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                               '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                            fileLines.insert(newCounter + 5, ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                                            counter += 2
                                            fileLines[newCounter + 6].append(codesList.laserLowPrinting)
                                            fileLines[newCounter + 6].append('(LASER LOW)')
                                            # 9fileLines[newCounter + 6].append('(fast move, c3)')
                                            break
                                        else:
                                            newCounter += 1
                                    break
                            pass
                        else:
                            tempCounter -= 1
                    except:
                        tempCounter -= 1

        # End of layer retracts (this WAS the most disgusting chunk of code ive ever written)
        if "(LAYER:" in fileLines[counter][1]:
                tempCounter = counter
                while True:
                    try:
                        if fileLines[tempCounter][4][0] == 'A':
                            if len(fileLines[tempCounter + 1]) < 5:
                                fileLines[tempCounter + 1].append(codesList.retractHigh)
                                fileLines[tempCounter + 1].append("(RETRACT HIGH)")
                                # fileLines[tempCounter + 1].append("(test)")
                                if fileLines[tempCounter + 2][3][0] == 'Y':
                                    if len(fileLines[tempCounter + 2]) == 4:
                                        fileLines[tempCounter + 2].append(codesList.retractLow)
                                        fileLines[tempCounter + 2].append("(RETRACT LOW)")
                                        fileLines.insert(tempCounter + 3, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                           '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                        counter += 1
                                        break
                                    else:
                                        fileLines.insert(tempCounter + 2, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                           '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                        fileLines.insert(tempCounter + 2, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                        counter += 2
                                        break
                                else:
                                    fileLines.insert(tempCounter + 2, ['NX', 'G04', 'P'+fileObject.fastWait,
                                                                       '(WAIT '+fileObject.fastWait+' MILLISECONDS)'])
                                    fileLines.insert(tempCounter + 2, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                    counter += 2
                                    break
                            else:
                                break
                        if 'F3600' in fileLines[tempCounter]:
                            if 'F600' in fileLines[tempCounter-1] or 'F600' in fileLines[tempCounter-2]:
                                fileLines.insert(tempCounter, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                fileLines.insert(tempCounter, ['NX', codesList.retractHigh, '(RETRACT HIGH)'])
                                counter += 2
                                break
                            tempCounter -= 1
                        else:
                            if fileLines[tempCounter][5][0] == 'A':
                                fileLines.insert(tempCounter+2, ['NX', 'G04', 'P' + fileObject.fastWait,
                                                                 '(WAIT ' + fileObject.fastWait + ' MILLISECONDS)'])
                                fileLines.insert(tempCounter+2, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                                fileLines.insert(tempCounter+2, ['NX', codesList.retractHigh, '(RETRACT HIGH)'])
                                counter += 3
                                break
                            else:
                                tempCounter -= 1
                    except:
                        tempCounter -= 1

        # Beginning of layer wait and laser codes
        if "(LAYER:" in fileLines[counter][1]:
            tempCounter = counter
            while True:
                if len(fileLines[tempCounter]) == 2:
                    tempCounter += 1
                    continue
                if fileLines[tempCounter][2] == 'F600':
                    fileLines.insert(tempCounter, ['NX', codesList.laserHighPrinting, '(LASER HIGH)'])
                    fileLines.insert(tempCounter, ['NX', 'G04', 'P' + fileObject.layerWait,
                                                       '(WAIT ' + fileObject.layerWait + ' MILLISECONDS)'])
                    counter += 2
                    fileLines[tempCounter + 2].append(codesList.laserLowPrinting)
                    fileLines[tempCounter + 2].append('(LASER LOW)')
                    break
                else:
                    tempCounter += 1

        # In the future, if we need different macros for different speeds, use this
        """
        #  Change feed speed of outer wall moves
        if "(TYPE:WALL-OUTER)" in fileLines[counter][1]:
            if fileLines[counter + 1][2][0] == 'F':
                fileLines[counter + 1][2] = 'F510'
        """

        counter += 1
        skip = False
        option = False

    # Weird fix for retract high/low
    counter = fileObject.warmedEnd
    while counter < len(fileLines):
        if "(RETRACT HIGH)" in fileLines[counter]:
            if '(RETRACT LOW)' not in fileLines[counter+1]:
                fileLines.insert(counter+1, ['NX', codesList.retractLow, '(RETRACT LOW)'])
                counter += 1
                pass
        counter += 1

    # Adding of M01 stop commands at layer changes
    counter = 0
    while counter < len(fileLines) - 1:
        if len(fileLines[counter]) > 3:
            counter += 1
            continue
        else:
            if "(LAYER:" in fileLines[counter][1]:
                # fileLines[counter].append('M01')
                # fileLines[counter].append('(OPTIONAL STOP)')
                fileLines.insert(counter+1, ['NX', 'M01', '(OPTIONAL STOP)'])
            counter += 1

    # Creation of list to be exported
    for lines in fileLines:
        newLines.append(lines)

    return newLines
# -----------------------------------------------


# PASS 6 ----------------------------------------
def removeAndReplace(fileLines, fileObject, codesList):
    """
        Name: removeAndReplace() - PASS 6
            This function is used to apply the finishing touches to the file before being
            exported by removing or replacing new line characters, Z values, lines #'s, and
            A codes.
    :param fileLines: a list of file lines
    :param fileObject: an object file with variables relating to the input and output file
    :param codesList: a list of Meltio specific M codes
    :return: newLines: a new list of lines with changes done to them
    """

    # Removes \n from any segment
    tempList = []
    for lines in fileLines:
        segmentList = []
        for segments in lines:
            newSegments = segments.strip()
            segmentList.append(newSegments)

        tempList.append(segmentList)

    newLines = tempList

    # Redetermine warming layer (because it somehow got skewed and im too lazy to go and find where)
    counter = 0
    while True:
        if '(LAYER:0)' in newLines[counter]:
            fileObject.warmedEnd = counter - 1
            break
        counter += 1

    # Remove any extra commands in warming layer
    counter = fileObject.warmedEnd
    while newLines[counter][1] != '(-----------)':
        for segment in newLines[counter]:
            if segment[0] == 'M':
                if segment == codesList.laserHighWarming or segment == codesList.laserLowWarming:
                    pass
                else:
                    if len(newLines[counter]) < 4:
                        newLines.pop(counter)
                        continue
                    else:
                        newLines[counter].pop()
                        newLines[counter].pop()
        counter -= 1

    # TODO: fix macro replacements
    # Outer macro replacement
    # newLines = macroReplacement(1, fileObject, codesList, newLines)

    # Inner macro replacement
    # newLines = macroReplacement(2, fileObject, codesList, newLines)

    # Fill macro replacement
    # newLines = macroReplacement(3, fileObject, codesList, newLines)

    # Printing the tool paths? Purely experimental
    # newLines = coordinateList(newLines)

    # Add breaks for machining
    # TODO: rework machining break code to work for any layer/machining height
    temp = []
    counter = 0
    maxHeight = float(fileObject.layerHeight) * float(fileObject.layerCount)
    machiningHeight = float(getMachiningHeight())
    while newLines[counter][1] != '%':
        if counter < fileObject.warmedEnd:
            pass
        else:
            for segment in newLines[counter]:
                if 'Z' in segment:
                    if ":" in segment:
                        pass
                    elif "M00" in newLines[counter+1]:
                        pass
                    else:
                        try:
                            currentHeight = round(float(segment.split("Z")[1]) - float(fileObject.layerHeight), 1)
                            if currentHeight >= float(machiningHeight):
                                while True:
                                    if 'LAYER' not in newLines[counter][1]:
                                        temp.append(newLines[counter])
                                        counter += 1
                                    else:
                                        temp.append(['NX', codesList.chillerLow, '(CHILLER OFF)'])
                                        temp.append(['NX', codesList.argonLow, '(ARGON OFF)'])
                                        temp.append(['NX', 'M01'])
                                        temp.append(['NX', 'G55'])
                                        temp.append(['NX', '(--MACHINING START--)'])
                                        temp.append(['NX', '(--MACHINING END--)'])
                                        temp.append(['NX', 'G54'])
                                        temp.append(['NX', codesList.argonHigh, '(ARGON ON)'])
                                        temp.append(['NX', codesList.chillerHigh, '(CHILLER ON)'])
                                        machiningHeight += float(getMachiningHeight())
                                        break

                        except:
                            pass

        temp.append(newLines[counter])
        counter += 1

    temp.append(newLines[counter])
    newLines = temp

    """
    # Adding FANUC shit
    counter = 0
    while counter<len(newLines)-1:
        if '(--MACHINING START--)' in newLines[counter]:
            newLines.insert(counter, ['NX', codesList.chillerLow, '(CHILLER OFF)'])
            counter += 1
        counter += 1
    """

    # Remove any laser high/lows at end of layer
    counter = fileObject.warmedEnd + 1
    while counter < len(newLines):
        if '(LAYER' in newLines[counter][1]:
            tempCounter = counter - 1
            while True:
                if 'F3600' in newLines[tempCounter]:
                    break
                else:
                    if newLines[tempCounter][1][0] == 'M':
                        newLines.pop(tempCounter)
                    elif '(LASER LOW)' in newLines[tempCounter]:
                        newLines[tempCounter].pop()
                        newLines[tempCounter].pop()
                    tempCounter -= 1

        counter += 1

    # Remove all A codes
    for lines in newLines:
        segmentCounter = 0
        for segments in lines:
            if segments[0] == 'A':
                lines.pop(segmentCounter)
            segmentCounter += 1

    return newLines
# -----------------------------------------------


# PASS 7 ----------------------------------------
def comments(fileLines, fileObject, codesList):
    """
        Name: comments()
            This function is used to add comments to the processed file to allow
            for easier reading and for easier manual troubleshooting.
    :param fileLines: a list of file lines
    :param fileObject: an object file with variables relating to the input and output file
    :param codesList: a list of Meltio specific M codes
    :return: newLines: a new list of line with changes done to them
    """
    newLines = []
    fileObject.noLayers = 0
    retractHigh, retractLow, laserHigh, laserLow = 0, 0, 0, 0

    # Fix for last laser low and high, needs to be added here to do at end of file
    counter = len(fileLines) - 1
    high = False
    low = False
    while True:
        for segment in fileLines[counter]:
            if high and low:
                break
            if segment == codesList.laserHighPrinting:
                fileLines.pop(counter)
                fileLines.pop(counter)
                high = True
            if segment == codesList.laserLowPrinting:
                fileLines[counter].pop()
                fileLines[counter].pop()
                low = True
        counter -= 1

        if high and low:
            break

    # Counts for certain values
    for line in fileLines:
        if "(LAYER:" in line:
            fileObject.noLayers += 1
        if '(RETRACT HIGH)' in line:
            retractHigh += 1
        if '(RETRACT LOW)' in line:
            retractLow += 1
        if 'M102' in line:
            laserHigh += 1
        if 'M202' in line:
            laserLow += 1

    counter = 0
    waitTime = 0
    for lines in fileLines:
        for segment in lines:
            if '(WAIT' in segment:
                timeValue = segment.split(' ')[1]
                waitTime += int(timeValue)

        # Add post-processor to generated comment
        if "(GENERATED" in lines:
            lines[4] = lines[4][:-1]
            lines.append("+")
            lines.append("POST")
            lines.append("PROCESSOR)")

            # Inserting lines with relevant info
            newLines.insert(counter, ['NX', '(# OF RETRACT LOW: %2d)' % retractLow])
            newLines.insert(counter, ['NX', '(# OF RETRACT HIGH: %2d)' % retractHigh])
            newLines.insert(counter, ['NX', '(# OF LASER LOW: %2d)' % (laserLow)])
            newLines.insert(counter, ['NX', '(# OF LASER HIGH: %2d)' % (laserHigh)])

        counter += 1
        newLines.append(lines)

    # Time for Meltio to process laser and retract signals
    waitTime += (retractHigh * 2000)
    waitTime += (laserHigh * 2000)

    # Add Cura generated print time
    curaTime = str(newLines[1][1]).split(':')
    time = curaTime[1]
    time = time[:-1]
    time = int(time) * 1000
    waitTime += time

    # Convert to HH:MM:SS and add to file
    waitTimeSeconds = waitTime/1000
    s = waitTimeSeconds
    hours = s // 3600
    s = s - (hours * 3600)
    minutes = s // 60
    seconds = s - (minutes * 60)
    newLines[1].pop()
    newLines[1].append('(PRINT TIME: {:02}H:{:02}M:{:02}S)'.format(int(hours), int(minutes), int(seconds)))

    # Replace line numbers with final line numbers
    counter = int(10)
    for line in newLines:
        line[0] = "N" + str(counter)
        counter += 10

    return newLines
# -----------------------------------------------


# PASS 8 ----------------------------------------
def writeNewFile(fileObject):
    """
        Name: writeNewFile() - PASS 8
            This function is used to write the post processed input file to the user named
            output file. It opens a file with exportFilename.nc, adds the FANUC file number
            first, and then writes out the post processed lines.
    :param fileObject: an object file with variables relating to the input and output file
    """
    directory = "./Gcode/" + fileObject.exportFilename + ".nc"
    openedFile = open(directory, 'w')

    openedFile.write(fileObject.fileNumber + "\n")
    for line in fileObject.fileLines:
        openedFile.write(" ".join(line) + "\n")

    print("Total Lines: " + str(len(fileObject.fileLines)))
    openedFile.close()
    return
# -----------------------------------------------
