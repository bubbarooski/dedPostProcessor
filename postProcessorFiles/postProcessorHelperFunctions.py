"""
    This file is used by the post-processor, specifically in the macro replacement stage. Rather than
    copying and pasting the code a bunch of times, just put it in a single function.
    FUNCTIONS:
        macroReplacement()
"""

import numpy as np
from matplotlib import pyplot as plt


def macroReplacement(mode, fileObject, codesList, lines):
    """
        Name: macroReplacement()
            This function is used to replace the standard printing macros with the corresponding
            outer, inner, and fill macros. This function takes a mode to determine what macro it
            is replacing.
        :param mode: used to determine which macro is doing the replacing
        :param fileObject: an object file with variables relating to the input and output file
        :param codesList: a list of Meltio specific M codes
        :param lines: a list of file lines
        :return: lines: the newly modified lines
    """

    # 1 = outer, 2 = inner, 3 = fill
    if mode == 1:
        goodType = 'TYPE:WALL-OUTER'
        badType1 = 'TYPE:FILL'
        badType2 = 'TYPE:WALL-INNER'
        macroHigh = codesList.outerWallHigh
        macroLow = codesList.outerWallLow
    if mode == 2:
        goodType = 'TYPE:WALL-INNER'
        badType1 = 'TYPE:WALL-OUTER'
        badType2 = 'TYPE:FILL'
        macroHigh = codesList.innerWallHigh
        macroLow = codesList.innerWallLow
    if mode ==3:
        goodType = 'TYPE:FILL'
        badType1 = 'TYPE:WALL-OUTER'
        badType2 = 'TYPE:WALL-INNER'
        macroHigh = codesList.fillHigh
        macroLow = codesList.fillLow


    try:
        if macroHigh is None:
            pass
        else:
            counter = fileObject.warmedEnd
            block = False
            while counter < len(lines):
                if goodType in lines[counter][1]:
                    if not block:
                        block = True
                if block:
                    if "M102" in lines[counter][1]:
                        lines[counter][1] = macroHigh
                    if "M202" in lines[counter][1]:
                        lines[counter][1] = macroLow
                    if goodType in lines[counter][1]:
                        if "(LAYER" in lines[counter - 1][1]:
                            pass
                        else:
                            tempCounter = counter - 1
                            while True:
                                if lines[tempCounter][1][0] == 'M':
                                    lines[tempCounter - 1][1] = macroHigh
                                    lines[tempCounter][1] = macroLow
                                    break
                                else:
                                    tempCounter -= 1
                if badType1 in lines[counter][1] or badType2 in lines[counter][1]:
                    block = False
                counter += 1
    except:
        pass

    return lines


def coordinateList(lines):

    # Find minimums
    xList, yList, zList = [], [], []
    zNum = 0
    counter = 0
    startFound = False
    for line in lines:
        for segment in line:
            if '(LAYER:0' in segment:
                startFound = True

            if '(MINX' in segment:
                number = segment.split(':')[1]
                xMin = number.split(')')[0]
                xList.append(xMin)

            if '(MINY' in segment:
                number = segment.split(':')[1]
                yMin = number.split(')')[0]
                yList.append(yMin)

            if '(MINZ' in segment:
                number = segment.split(':')[1]
                zMin = number.split(')')[0]
                zList.append(zMin)
                zNum = zMin

        if not startFound:
            counter += 1

    while True:
        newZ = False

        # End of code reached
        if '%' in lines[counter][1]:
            break

        # Any line this length does not have coordinates we need
        if len(lines[counter]) < 5:
            counter += 1
            continue

        for segment in lines[counter]:
            if 'X' in segment:
                if 'N' in segment:
                    pass
                else:
                    xNum = segment.split('X')[1]
                    # print(xNum)
                    xList.append(xNum)

            if 'Y' in segment:
                if 'TYPE' in segment:
                    pass
                else:
                    yNum = segment.split('Y')[1]
                    yList.append(yNum)

            if 'Z' in segment:
                zNum = segment.split('Z')[1]
                zList.append(zNum)
                newZ = True

        # Checking if new Z height was found and if not append existing z height
        if newZ:
            pass
        else:
            zList.append(zNum)

        counter += 1

    print('X list size: ' + str(len(xList)))
    print('Y list size: ' + str(len(yList)))
    print('Z list size: ' + str(len(zList)))

    floatXList = [float(i) for i in xList]
    floatYList = [float(i) for i in yList]
    floatZList = [float(i) for i in zList]

    coordinates = np.column_stack((floatXList, floatYList, floatZList))
    xC, yC, zC = coordinates.T

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plot = ax.plot(xC, yC, zC)

    """
    def update(frame):
        x = xC[:frame]
        y = yC[:frame]
        z = zC[:frame]
        
        data = np.stack([x,y,z]).T
        plot.set_offsets(data)
    """


    fig.set_size_inches(14,14)
    plt.show()

    return lines
