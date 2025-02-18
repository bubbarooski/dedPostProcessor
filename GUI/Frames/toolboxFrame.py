"""
    This file contains all pieces of the frame housing the toolbox.
        IMPORTS:
            tkinter
            customtkinter
            PIL.Image
            Config.macroGet
        FUNCTIONS:
            toolboxFrame()
                toolBoxTextCreation()
                saveAll()
                toolBoxFrameCreation()
                printMacros()

"""

import tkinter
import customtkinter as ctk
from PIL import Image
import Config.macroGet


def toolboxFrame(self):
    """
        Name: toolboxFrame
            This function acts as a driver function for entire toolbox
        :param self: the app as a whole
    """

    def toolBoxTextCreation():
        """
            Name: toolBoxTextCreation()
                This function creates the toolbox textbox.
        """
        self.toolboxText = ctk.CTkTextbox(self.toolboxFrame, width=305, height=225, fg_color='white',
                                          text_color='black', border_width=2, border_color="#f99d2a")
        self.toolboxText.grid(row=1, column=0, padx=10, sticky=ctk.N)

    def saveAll():
        """
            Name: saveAll()
                This function creates the save all button.
        """

        print = ctk.CTkImage(Image.open(".\images\print.png"), size=(22, 22))
        self.fillSave = ctk.CTkButton(self.toolboxFrame, text='Print macros', width=25, border_spacing=0, image=print,
                                      fg_color='white', text_color='black', hover=True, command=lambda: printMacros(self))
        self.fillSave.grid(row=0, column=0, sticky=ctk.W, padx=10, pady=10)

    def toolBoxFrameCreation():
        """
            Name: toolBoxFrameCreation()
                This function creates the frame and text box for the toolbox.
        """

        self.toolboxTitleBlock = ctk.CTkButton(self, text=' Toolbox Menu ', fg_color='black',
                                               font=('calibri BOLD', 20), width=50, height=25, anchor='w',
                                               border_width=2, border_color="#f99d2a", text_color='white',
                                               hover=False)
        self.toolboxTitleBlock.grid(row=2, column=0, sticky=ctk.NW, padx=120, pady=415)
        self.toolboxFrame = ctk.CTkFrame(self, width=325, height=285, border_width=2, fg_color='#4b6895', border_color="#f99d2a")
        self.toolboxFrame.grid_propagate(False)
        self.toolboxFrame.grid(row=2, column=0, columnspan=3, sticky=ctk.NW, padx=25, pady=460)
        self.toolboxFrame.grid_columnconfigure(3, weight=1)

        toolBoxTextCreation()
        saveAll()

    def printMacros(self):
        """
            Name: printMacros()
                This function is used to print all macros to the toolbox.
            :param self: the app as a whole
        """

        self.toolboxText.configure(state='normal')
        self.toolboxText.delete('1.0', tkinter.END)

        line = 'Fast wait time: ' + Config.macroGet.getFast() + 'ms'
        self.toolboxText.insert(tkinter.END, line + '\n')
        line = 'Layer wait time: ' + Config.macroGet.getLayer() + 'ms'
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getArgon()
        line = 'Argon macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getPrinting()
        line = 'Printing macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getRetract()
        line = 'Retract macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getWarming()
        line = 'Warming macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getOuter()
        line = 'Outer wall macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getInner()
        line = 'Inner wall macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        high, low = Config.macroGet.getFill()
        line = 'Fill macros: ' + high + ' and ' + low
        self.toolboxText.insert(tkinter.END, line + '\n')

        # value = Config.macroGet.

        self.toolboxText.configure(state='disabled')

    toolBoxFrameCreation()
