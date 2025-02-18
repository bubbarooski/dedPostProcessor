"""
    This file is the driver function for most things related to the macros.
        IMPORTS:
            Config.macroUpdate
            Config.parse
        FUNCTIONS:
            macroMenu()
            printMacros()
"""

import Config.macroSet as update
import Config.parse as parse


def macroMenu(codesList):
    """
        Name: macroMenu()
            This function prints out and controls the flow of the custom macro process.
        :param codesList: a list of all macros
        :return: codesList: a list of all updated codes
    """

    while True:
        print()
        print("--MACROS--")
        print("   1: Outer Wall")
        print("   2: Inner Wall")
        print("   3: Fill")
        print("   4: Print Macros")
        print("  -1: Back")

        userInput = input("Please enter choice: ")

        try:
            # Outer Wall
            if int(userInput) == 1:
                outerMacro = input("Enter macro number for outer wall (1-7): ")
                outerMacroHigh = 'M10' + outerMacro
                outerMacroLow = 'M20' + outerMacro
                codesList = update.setOuter(codesList, outerMacroHigh, outerMacroLow)

            # Inner Wall
            elif int(userInput) == 2:
                innerMacro = input("Enter macro number for inner wall (1-7): ")
                innerMacroHigh = 'M10' + innerMacro
                innerMacroLow = 'M20' + innerMacro
                codesList = update.setInner(codesList, innerMacroHigh, innerMacroLow)

            # Fill
            elif int(userInput) == 3:
                fillMacro = input("Enter macro number for fill (1-7): ")
                fillMacroHigh = 'M10' + fillMacro
                fillMacroLow = 'M20' + fillMacro
                codesList = update.setFill(codesList, fillMacroHigh, fillMacroLow)

            # Printing all macros
            elif int(userInput) == 4:
                printMacros()

            # Exit
            elif int(userInput) == -1:
                return codesList
            else:
                print("--INVALID MACRO MENU CHOICE--")
                continue
        except:
            print("--INVALID MACRO MENU ENTRY--")
            continue


def printMacros():
    """
        Name: printMacros()
            This functions prints out all current macros
    """
    dictionary = parse.parameterDictionary

    print()
    print("--LIST OF MACROS--")
    print("Outer wall high: " + dictionary['outerWallHigh'])
    print("Outer wall low: " + dictionary['outerWallLow'])
    print("Inner wall high: " + dictionary['innerWallHigh'])
    print("Inner wall low: " + dictionary['innerWallLow'])
    print("Fill high: " + dictionary['fillHigh'])
    print("Fill low: " + dictionary['fillLow'])
