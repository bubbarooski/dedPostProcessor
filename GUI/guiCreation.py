"""
    This file houses the App class and all of its function calls to build and run
    the GUI as a whole.
        IMPORTS:
            customtkinter
            GUI.Frames.logoFrame.snowbirdLogoFrame
            GUI.Frames.macroFrame.macroFrame
            GUI.Frames.toolboxFrame.toolboxFrame
            GUI.Frames.printingFileFrame.currentFileFrame
            GUI.Frames.machiningFileFrame.currentFileFrame
            GUI.Frames.processedFileFrame.processedFileFrame
            GUI.Frames.processedFileSettings.processedFileSettingsFrame
        CLASSES:
            App

"""

import customtkinter as ctk
from GUI.Frames.logoFrame import snowbirdLogoFrame
from GUI.Frames.macroFrame import macroFrame
from GUI.Frames.toolboxFrame import toolboxFrame
from GUI.Frames.printingFileFrame import printingFileFrame
from GUI.Frames.machiningFileFrame import machiningFileFrame
from GUI.Frames.processedFileFrame import processedFileFrame
from GUI.Frames.processedFileSettings import processedFileSettingsFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    """
        Name: App
            This class is used to store any and all parts related to the gui.
            Each frame has the associated parts of the gui and all related commands
            to do different things.
    """

    def __init__(self):
        super().__init__()

        # Window details ------------------------
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.title("DED Post Processor")
        self.configure(background='white')
        # ---------------------------------------

        snowbirdLogoFrame(self)
        macroFrame(self)
        toolboxFrame(self)
        printingFileFrame(self)
        machiningFileFrame(self)
        processedFileFrame(self)
        processedFileSettingsFrame(self)
