"""
    This file contains all pieces of the frame housing the machining selected file, pre-processed.
        IMPORTS:
            customtkinter
            PIL.Image
            tkinter.filedialog
            GUI.Frames.processedFileFrame.showProcessedFile
        FUNCTIONS:
            machiningFileFrame()
                openFileButton()
                machiningFileFrameCreation()
                arrowIcon()
                browseFiles()
"""

import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
from GUI.Frames.processedFileFrame import showProcessedFile


def machiningFileFrame(self):
    """
        Name: machiningFileFrame()
            This function acts as a driver function for the entire machining file frame.
        :param self: the app as a whole
    """

    def openFileButton():
        """
            Name: openFileButton()
                This function creates the open file button.
        """

        openFile = ctk.CTkImage(Image.open(".\images\openFile.png"), size=(30, 30))
        self.fillSave = ctk.CTkButton(self, text='Open Machining File', width=150, border_width=2, image=openFile,
                                      fg_color='#4b6895', border_color='#f99d2a', hover=True,
                                      font=('calibri BOLD', 16)
                                      # ,command=lambda: browseFiles(self)
                                      )
        self.fillSave.grid(row=2, column=0, sticky=ctk.NW, padx=760, pady=750)

    def machiningFileFrameCreation():
        """
            Name: machiningFileFrameCreation()
                This function creates the frame and text box for the machining file.
        """

        self.machiningFileTitleBlock = ctk.CTkButton(self, text=' Machining File ', fg_color='black',
                                                     font=('calibri BOLD', 20), width=50, height=25, anchor='w',
                                                     border_width=2, border_color="#f99d2a", text_color='white',
                                                     hover=False)
        self.machiningFileTitleBlock.grid(row=1, column=0, sticky=ctk.NW, padx=780)
        self.machiningFileFrame = ctk.CTkFrame(self, width=300, height=735, border_width=2, fg_color='transparent',
                                               border_color="#f99d2a")
        self.machiningFileFrame.grid_propagate(False)
        self.machiningFileFrame.grid(row=2, column=0, columnspan=1, sticky=ctk.NW, padx=705, pady=10)
        self.machiningFileText = ctk.CTkTextbox(self.machiningFileFrame, width=300, height=735, fg_color='black',
                                                text_color='white', border_width=2, border_color="#f99d2a")
        self.machiningFileText.grid(row=0, column=0)

    def browseFiles(self):
        """
            Name: browseFiles()
                This function is used to allow the user to browse g-code files to be processed
                and once one is selected, it is passed to another function for post processing.
            :param self: the app as a whole
        """

        self.machiningFileText.configure(state='normal')
        lines = self.machiningFileText.get('0.0', 'end')
        if len(lines) > 1:
            self.machiningFileText.delete('0.0', 'end')

        self.machiningFilename = filedialog.askopenfilename(initialdir="./Gcode/", title="Select a File",
                                                   filetypes=(("G-Code", "*.gcode*"), ("all files", "*.*")))

        file = open(self.machiningFilename, 'r')
        content = file.read()

        self.machiningFileText.insert('0.0', content)
        self.machiningFileText.configure(state='disabled')
        showProcessedFile(self)
        file.close()

    machiningFileFrameCreation()
    openFileButton()
