"""
    This file is used to run the gui and calls the driver function.
        IMPORTS:
            GUI.guiCreation.App
        FUNCTIONS:
            driver
"""

from GUI.guiCreation import App


def driver():
    """
        name: driver()
            This creates the App object and runs the gui loop.
    """

    app = App()
    app.mainloop()
