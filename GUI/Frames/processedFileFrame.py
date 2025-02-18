"""
    This file contains all pieces of the frame housing the post-processed file being displayed.
        IMPORTS:
            tkiter
            customtkinter
            postProcessingFiles.guiPostProcessing.guiPostProcess
        FUNCTIONS:
            processedFileFrame()
            processedFileFrameCreation()
            showProcessedFile()

"""

import tkinter
import customtkinter as ctk
from postProcessorFiles.guiPostProcessing import guiPostProcess


def processedFileFrame(self):
    """
        Name: processedFileFrame()
            This function acts as a driver function for the entire processed file frame.
        :param self: the app as a whole
    """

    def processedFileFrameCreation():
        """
            Name: processedFileFrameCreation()
                This function creates the frame and textbox for the processed file.
        """
        self.processedFileTitleBlock = ctk.CTkButton(self, text='Post-processed File', fg_color='black',
                                                     font=('calibri BOLD', 20), width=50, height=25, anchor='w',
                                                     border_width=2, border_color="#f99d2a", text_color='white',
                                                     hover=False)
        self.processedFileTitleBlock.grid(row=1, column=0, sticky=ctk.W, padx=1200)
        self.processedFileFrame = ctk.CTkFrame(self, width=450, height=735, border_width=2, fg_color='transparent',
                                               border_color="#f99d2a")
        self.processedFileFrame.grid_propagate(False)
        self.processedFileFrame.grid(row=2, column=0, columnspan=1, sticky=ctk.NW, pady=10, padx=1050)
        self.processedFileText = ctk.CTkTextbox(self.processedFileFrame, width=450, height=735, fg_color='black',
                                                text_color='white', border_width=2, border_color="#f99d2a")
        self.processedFileText.grid(row=0, column=0)

    processedFileFrameCreation()


def showProcessedFile(self):
    """
        Name: showProcessedFile()
            This function processes the file from a filename already saved and displays
            it in the textbox in this frame.
        :param self: the app as a whole
    """

    self.processedFileText.configure(state='normal')
    currentText = self.processedFileText.get('0.0', 'end')

    # Resets processedFileText if something is there
    if len(currentText) > 1:
        self.processedFileText.delete('0.0', 'end')

    self.lines = guiPostProcess(self.printingFilename)

    # print(self.printingFilename)
    # print(self.machiningFilename)

    # Printing newly post processed lines to screen
    for line in self.lines:
        self.processedFileText.insert(tkinter.END, ' '.join(line) + '\n')

    self.processedFileText.configure(state='disabled')
