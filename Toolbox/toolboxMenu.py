"""
    This file contains all functions related to the toolbox and the menu.
        IMPORTS:
            os
        FUNCTIONS:
            toolboxMenu()
"""

import os
import Toolbox.lineNumberReset as reset


def toolboxMenu():
    """
        Name: toolboxMenu()
            This function is used to print the menu and call the requisite scripts.

    """

    while True:
        print()
        print("--TOOLBOX--")
        print("   1: Reset line numbers")
        print("  -1: Back")

        userInput = input("Please enter choice: ")
        try:
            if int(userInput) == 1:
                reset.controlFlow()
            elif int(userInput) == -1:
                return
            else:
                print("--INVALID MAIN MENU CHOICE--")
                continue
        except Exception as toolBoxError:
            print("Toolbox menu error:", toolBoxError)
            print("--TOOLBOX MENU ENTRY--")
            continue
