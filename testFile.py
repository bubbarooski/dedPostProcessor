"""
    This file is a simple script to test the program without having to input values. As
    the number of user inputted values increases, it takes longer to run the program for
    tests so this file take care of that. It also lists elapsed time of total run.
    The imports, classes, and functions are listed
    below:
        IMPORTS:
            menuFunctions
            postProcess
            time
"""

from postProcessorFiles import postProcess
import time
import os


def inputFilename():
    """
        Name: inputFilename()
            This functions prints a list of valid gcode files in the /Gcode/ directory
            and asks the user to input which of the files they would like to be processed.
        :return: fileList[x-1]: where x-1 is the chosen file by the user
    """

    counter = 0
    fileList = []

    print("Files:")

    # Opens the directory and creates a list of all valid gcode files
    files = os.listdir("./Gcode/")
    for file in files:
        if file.endswith(".gcode"):
            counter = counter + 1
            fileList.append(file)
            print("%s) %s" % (counter, file))

    while True:
        userInput = input("Enter file number: ")
        try:
            if int(userInput) > len(fileList):
                print("--INVALID CHOICE--")
                continue
            else:
                return fileList[int(userInput) - 1]

        except:
            print("--INVALID CHOICE--")
            continue


fileName = inputFilename()
fileNumber = str(1234)
exportedFileName = "automatedTest"
layerWait = 100
fastWait = 5

# Creation of file object
fileObject = postProcess.file(fileName, fileNumber, exportedFileName, layerWait, fastWait)

print("Starting...")
startTime = time.time()
codesList = postProcess.codes()

postProcess.postProcessingControlFunction(fileObject, 0)

endTime = time.time()
elapsedTime = endTime - startTime
elapsedTime = round(elapsedTime, 3)

print("Exported")
print("Elapsed time:" + str(elapsedTime))
exit()
