"""
    This file is not related to the main program but is a standalone file that can reset
    the FANUC line numbers. This is designed to be standalone, so it uses none of the other
    functions that are previously written and combines everything into one file.
    You're welcome Nathan.
        Imports:
            os
"""

import os


def controlFlow():
    """
        Name: controlFlow()
            This file is used to control the flow of the script
    """
    # checkValidNC()
    reset()


def checkValidNC():
    """
        Name: checkValidNC()
            This function is used to check if the file to be passed through the
            renumbering script is a valid .nc file.
    """
    pass
    """
    # TODO: incorporate function
    """


def reset():
    """
        Name: reset
            This function is used to run the script to renumber lines for a
            VALID .nc file
    """
    fileList = []
    lineList = []
    newLineList = []
    counter = 0

    print("-------------------------------")
    print("   --FILE RENUMBERER--")

    # Opens the directory and creates a list of all valid gcode files
    files = os.listdir("../curaDEDPostProcessor/Gcode")
    for file in files:
        if file.endswith(".nc"):
            counter = counter + 1
            fileList.append(file)
            print("%s) %s" % (counter, file))
    print("-------------------------------")

    while True:
        userInput = input("Enter file number: ")
        try:
            if int(userInput) > len(fileList):
                print("--INVALID CHOICE--")
                continue
            else:
                file = fileList[int(userInput) - 1]
                directory = "./Gcode/" + file
                openedFile = open(directory, 'r')

                lines = openedFile.readlines()

                # Open file and add each line to a list
                counter = 0
                for line in lines:
                    lineList.append(line)
                    counter = counter + 1

                for line in lineList:
                    splitLine = line.split(" ")
                    newLineList.append(splitLine)
                    counter = counter + 1

                counter = int(10)
                for lines in newLineList:
                    if lines[0][0] == 'N':
                        lines[0] = "N" + str(counter)
                        counter += 10
                    else:
                        continue

                openedFile = open(directory, 'w')
                for line in newLineList:
                    openedFile.write(" ".join(line))

                openedFile.close()
                print('File renumbered!')
                print()
                break

        except Exception as error:
            print("lineNumberReset error: ", error)
            print("--INVALID CHOICE--")
            continue


if __name__ == '__main__':
    controlFlow()
