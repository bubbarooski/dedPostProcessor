"""
    This file contains the functions and commands used in the processed file frame.
        IMPORTS:
            customtkinter
            PIL.Image
            postProcessorFiles.guiPostProcessing.guiWriteNewFile
        FUNCTIONS:
            processedFileSettingsFrame()
                fileNumber()
                saveFileButton()
                processedFileSettings()
                saveFile()
                fileNumberSaveButton()
"""

import customtkinter as ctk
from PIL import Image
from postProcessorFiles.guiPostProcessing import guiWriteNewFile
from Config.macroSet import setMachiningHeight


def processedFileSettingsFrame(self):
    """
        Name: processedFileSettingsFrame()
            This function creates the processed file settings frame and holds all requisite
            functions.
        :param self: the app as a whole
    """

    def fileNumber():
        """
            Name: fileNumber()
                This function creates the button and entry for the file number.
        """

        self.fileNumberText = ctk.CTkLabel(self.processedFileSettingsFrame, width=70, height=8, text='File Number',
                                           text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.fileNumberText.grid(row=1, column=0, sticky=ctk.W, padx=5, pady=10)
        self.fileNumberEntry = ctk.CTkEntry(self.processedFileSettingsFrame, width=170, fg_color='white', placeholder_text_color="black", text_color='#000000',
                                            placeholder_text="Enter file number")
        self.fileNumberEntry.grid(row=1, column=1, sticky=ctk.W)
        fileNumberSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.fileNumberSave = ctk.CTkButton(self.processedFileSettingsFrame, text='', width=25, border_spacing=0, image=fileNumberSave,
                                            fg_color='transparent', hover=True, command=lambda: fileNumberSaveButton(self))
        self.fileNumberSave.grid(row=1, column=2, sticky=ctk.W)

    def user():
        """
            Name: user()
                This function creates the button and entry for the user.
        """

        self.userText = ctk.CTkLabel(self.processedFileSettingsFrame, width=70, height=8, text='             User',
                                           text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.userText.grid(row=2, column=0, sticky=ctk.E, padx=5, pady=10)
        self.userEntry = ctk.CTkOptionMenu(self.processedFileSettingsFrame, width=170, height=25, fg_color='white', button_color=('black', 'white'),
                                           dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                           text_color='black', hover=False, values=['---', 'User 1', 'User 2', 'User 3', 'User 4',
                                                                                    'User 5'])
        self.userEntry.grid(row=2, column=1, sticky=ctk.W)
        userSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.userSave = ctk.CTkButton(self.processedFileSettingsFrame, text='', width=25, border_spacing=0, image=userSave,
                                            fg_color='transparent', hover=True, command= lambda: userSaveButton(self))
        self.userSave.grid(row=2, column=2, sticky=ctk.W)

    def machiningCheck():
        self.machiningBreakText = ctk.CTkLabel(self.processedFileSettingsFrame, width=70, height=8, text=' Machining',
                                               text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.machiningBreakText.grid(row=3, column=0, sticky=ctk.NE, padx=5, pady=0)
        self.machiningBreakEntry = ctk.CTkCheckBox(self.processedFileSettingsFrame, width=170, onvalue="on",
                                                   offvalue="off", border_color='black', text='Toggle for machining',
                                                   text_color='white', font=('calibri BOLD', 14))
        self.machiningBreakEntry.grid(row=3, column=1, sticky=ctk.NW)
        """
        userSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.machiningBreakSave = ctk.CTkButton(self.processedFileSettingsFrame, text='', width=25, border_spacing=0, image=userSave,
                                            fg_color='transparent', hover=True,command=lambda: machiningBreakSaveButton(self))
        self.machiningBreakSave.grid(row=3, column=2, sticky=ctk.W)
        """

    def saveFileButton():
        """
            Name: saveFileButton()
                This function creates the save file button.
        """

        save = ctk.CTkImage(Image.open(".\images\save.png"), size=(30, 30))
        self.fillSave = ctk.CTkButton(self, text='Save File', width=150, border_width=2, image=save,
                                      fg_color='#4b6895', border_color='#f99d2a', hover=True,
                                      font=('calibri BOLD', 14), command=lambda: saveFile(self))
        self.fillSave.grid(row=2, column=0, sticky=ctk.NW, padx=1650, pady=180)

    def processedFileSettings():
        """
            Name: processedFileSettings()
                This function creates the frame for file settings and calls the other pieces.
        """

        self.processedFileSettingsTitleBlock = ctk.CTkButton(self, text='File Settings', fg_color='black',
                                                             font=('calibri BOLD', 20), width=50, height=25, anchor='w',
                                                             border_width=2, border_color="#f99d2a", text_color='white',
                                                             hover=False)
        self.processedFileSettingsTitleBlock.grid(row=1, column=0, sticky=ctk.NW, padx=1660)
        self.processedFileSettingsFrame = ctk.CTkFrame(self, width=300, height=130, border_width=2, fg_color='#4b6895', border_color="#f99d2a")
        self.processedFileSettingsFrame.grid_propagate(False)
        self.processedFileSettingsFrame.grid(row=2, column=0, columnspan=1, sticky=ctk.NW, pady=10, padx=1570)

        fileNumber()
        saveFileButton()
        user()
        machiningCheck()

    def saveFile(self):
        """
            Name: saveFile()
                This function will check if a file number has been added and if so, save the file.
            :param self: the app as a whole
        """

        if hasattr(self, 'fileNumber') and hasattr(self, 'user'):
            guiWriteNewFile(self)
            self.exportText = ctk.CTkLabel(self, width=100, height=12, text='File exported successfully!',
                                           text_color='white', fg_color='transparent', font=('calibri BOLD', 20), justify='left')
            self.exportText.grid(row=2, column=0, sticky=ctk.N, padx=1600, pady=240)
            self.exportText.after(3000, self.exportText.destroy)
        else:
            print('no')
            self.fileErrorText = ctk.CTkLabel(self.processedFileSettingsFrame, width=100, height=8, text='Missing value!',
                                              text_color='red', fg_color='transparent', font=('calibri BOLD', 14), justify='left')
            self.fileErrorText.grid(row=4, column=1, sticky=ctk.W)
            self.fileErrorText.after(3000, self.fileErrorText.destroy)

    def fileNumberSaveButton(self):
        """
            Name: fileNumberSaveButton()
                This function flashes the text "File number added!" when the file number is saved.
            :param self: the app as a whole
        """

        self.fileNumber = self.fileNumberEntry.get()
        self.fileNumberText = ctk.CTkLabel(self.processedFileSettingsFrame, width=100, height=8, text='File number added!',
                                          text_color='white', fg_color='transparent', font=('calibri BOLD', 14), justify='left')
        self.fileNumberText.grid(row=4, column=1, sticky=ctk.SW)
        self.fileNumberText.after(3000, self.fileNumberText.destroy)

    def userSaveButton(self):
        self.user = self.userEntry.get()
        self.fileNumberText = ctk.CTkLabel(self.processedFileSettingsFrame, width=150, height=8, text='User added!',
                                           text_color='white', fg_color='transparent', font=('calibri BOLD', 14), justify='left')
        self.fileNumberText.grid(row=4, column=1, sticky=ctk.SW)
        self.fileNumberText.after(3000, self.fileNumberText.destroy)

    def machiningBreakSaveButton(self):
        self.machiningHeight = self.machiningBreakEntry.get()
        setMachiningHeight(self.machiningHeight)
        self.fileNumberText = ctk.CTkLabel(self.processedFileSettingsFrame, width=150, height=8, text='Machining height added!',
                                           text_color='white', fg_color='transparent', font=('calibri BOLD', 14), justify='left')
        self.fileNumberText.grid(row=4, column=1, sticky=ctk.SW)
        self.fileNumberText.after(3000, self.fileNumberText.destroy)

    processedFileSettings()
