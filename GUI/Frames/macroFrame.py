"""
    This file contains all piece of the frame housing the macros, and the functions that control them.
        IMPORTS:
            customtkinter
            PIL.Image
            GUI.Functions.macroFunctions
        FUNCTIONS:
            macroFrame()
                fastMove()
                layerMove()
                argonMacro()
                printingMacro()
                retractMacro()
                warmingMacro()
                outerWallMacro()
                innerWallMacro()
                fillMacro()
                saveAll()
                macroFrameCreation()
                fastMoveButton()
                layerMoveButton()
                argonButton()
                printingButton()
                retractButton()
                warmingButton()
                outerWallButton()
                innerWallButton()
                fillButton()
                saveAllButton()

"""

import customtkinter as ctk
from PIL import Image
import GUI.Functions.macroFunctions as commands


def macroFrame(self):
    """
        Name: macroFrame()
            This function acts as a driver function for the entire macro frame. It houses the
            macro entry boxes as well as the commands that are used when a new macro is saved.
        :param self: the app as a whole
    """

    # Macros --------------------------------
    def fastMove():
        """
            Name: fastMove()
                This function creates the fast move macro entry and save button.
        """

        self.fastMoveText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text='Fast Move Wait:', corner_radius=2,
                                         text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.fastMoveText.grid(row=0, column=0, sticky=ctk.E, padx=10, pady=10)
        self.fastMoveEntry = ctk.CTkEntry(self.macroFrame, width=150, fg_color='white', placeholder_text_color="#000000", text_color='#000000',
                                          placeholder_text="Enter time in ms")
        self.fastMoveEntry.grid(row=0, column=1, sticky=ctk.W)
        fastMoveSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.fastMoveSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=fastMoveSave,
                                          fg_color='transparent', hover=True, command=fastMoveButton)
        self.fastMoveSave.grid(row=0, column=2, sticky=ctk.W)

    def layerMove():
        """
            Name: layerMove()
                This function creates the layer move macro entry and save button.
        """

        self.layerMoveText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text='Layer Move Wait:', corner_radius=2,
                                          text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.layerMoveText.grid(row=1, column=0, sticky=ctk.E, padx=10, pady=10)
        self.layerMoveEntry = ctk.CTkEntry(self.macroFrame, width=150, fg_color='white', placeholder_text_color="#000000",
                                           placeholder_text="Enter time in ms")
        self.layerMoveEntry.grid(row=1, column=1, sticky=ctk.W)
        layerMoveSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.layerMoveSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=layerMoveSave,
                                           fg_color='transparent', hover=True, command=layerMoveButton)
        self.layerMoveSave.grid(row=1, column=2, sticky=ctk.W)

    def argonMacro():
        """
            Name: argonMacro()
                This function creates the argon macro entry and save button.
        """

        self.argonText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text='  Argon Macro:',
                                      text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.argonText.grid(row=2, column=0, sticky=ctk.E, padx=10, pady=10)
        self.argonEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                            dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                            text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                     'Macro 5', 'Macro 6', 'Macro 7'])
        self.argonEntry.grid(row=2, column=1, sticky=ctk.W)
        argonSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.argonSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=argonSave,
                                       fg_color='transparent', hover=True, command=argonButton)
        self.argonSave.grid(row=2, column=2, sticky=ctk.W)

    def printingMacro():
        """
            Name: printingMacro()
                This function creates the printing macro entry and save button.
        """

        self.printingText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text='  Printing Macro:',
                                         text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.printingText.grid(row=3, column=0, sticky=ctk.E, padx=10, pady=10)
        self.printingEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                               dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                               text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                        'Macro 5', 'Macro 6', 'Macro 7'])
        self.printingEntry.grid(row=3, column=1, sticky=ctk.W)
        printingSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.printingSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=printingSave,
                                          fg_color='transparent', hover=True, command=printingButton)
        self.printingSave.grid(row=3, column=2, sticky=ctk.W)

    def retractMacro():
        """
            Name: retractMacro()
                This function create the retract macro entry and save button.
        """

        self.retractText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text=' Retract Macro:',
                                        text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.retractText.grid(row=4, column=0, sticky=ctk.E, padx=10, pady=10)
        self.retractEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                              dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                              text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                       'Macro 5', 'Macro 6', 'Macro 7'])
        self.retractEntry.grid(row=4, column=1, sticky=ctk.W)
        retractSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.retractSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=retractSave,
                                         fg_color='transparent', hover=True, command=retractButton)
        self.retractSave.grid(row=4, column=2, sticky=ctk.W)

    def warmingMacro():
        """
            Name: warmingMacro()
                This function create the warming macro entry and save button.
        """

        self.warmingText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text=' Warming Macro:',
                                        text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.warmingText.grid(row=5, column=0, sticky=ctk.E, padx=10, pady=10)
        self.warmingEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                              dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                              text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                       'Macro 5', 'Macro 6', 'Macro 7'])
        self.warmingEntry.grid(row=5, column=1, sticky=ctk.W)
        warmingSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.warmingSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=warmingSave,
                                         fg_color='transparent', hover=True, command=warmingButton)
        self.warmingSave.grid(row=5, column=2, sticky=ctk.W)

    def outerWallMacro():
        """
            Name: outerWallMacro()
                This function creates the outer wall macro entry and save button.
        """

        self.outerWallText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text=' Outer Wall Macro:',
                                          text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.outerWallText.grid(row=6, column=0, sticky=ctk.E, padx=10, pady=10)
        self.outerWallEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                                dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                                text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                         'Macro 5', 'Macro 6', 'Macro 7'])
        self.outerWallEntry.grid(row=6, column=1, sticky=ctk.W)
        outerWallSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.outerWallSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=outerWallSave,
                                           fg_color='transparent', hover=True, command=outerWallButton)
        self.outerWallSave.grid(row=6, column=2, sticky=ctk.W)

    def innerWallMacro():
        """
            Name: innerWallMacro()
                This function creates the inner wall macro entry and save button.
        """

        self.innerWallText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text=' Inner Wall Macro:',
                                          text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.innerWallText.grid(row=7, column=0, sticky=ctk.E, padx=10, pady=10)
        self.innerWallEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                                dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                                text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                         'Macro 5', 'Macro 6', 'Macro 7'])
        self.innerWallEntry.grid(row=7, column=1, sticky=ctk.W)
        innerWallSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.innerWallSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=innerWallSave,
                                           fg_color='transparent', hover=True, command=innerWallButton)
        self.innerWallSave.grid(row=7, column=2, sticky=ctk.W)

    def fillMacro():
        """
            Name: fillMacro()
                This function creates the fill macro entry and save button.
        """

        self.fillText = ctk.CTkLabel(self.macroFrame, width=90, height=8, text='            Fill Macro:',
                                     text_color='#ffffff', fg_color='transparent', font=('calibri BOLD', 14), justify='right')
        self.fillText.grid(row=8, column=0, sticky=ctk.E, padx=10, pady=10)
        self.fillEntry = ctk.CTkOptionMenu(self.macroFrame, width=150, height=25, fg_color='white', button_color=('black', 'white'),
                                           dropdown_fg_color='white', dropdown_hover_color='#c5c5c5', dropdown_text_color='black',
                                           text_color='black', hover=False, values=['Macro 1', 'Macro 2', 'Macro 3', 'Macro 4',
                                                                                    'Macro 5', 'Macro 6', 'Macro 7'])
        self.fillEntry.grid(row=8, column=1, sticky=ctk.W)
        fillSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.fillSave = ctk.CTkButton(self.macroFrame, text='', width=25, border_spacing=0, image=fillSave,
                                      fg_color='transparent', hover=True, command=fillButton)
        self.fillSave.grid(row=8, column=2, sticky=ctk.W)

    def saveAll():
        """
            Name: saveAll()
                This function creates the save all button.
        """

        fillSave = ctk.CTkImage(Image.open(".\images\save.png"), size=(22, 22))
        self.fillSave = ctk.CTkButton(self.macroFrame, text='Save All', width=25, border_spacing=0, image=fillSave,
                                      fg_color='white', text_color='black', hover=True, command=saveAllButton)
        self.fillSave.grid(row=9, column=1, sticky=ctk.W)

    def macroFrameCreation():
        """
            Name: macroFrameCreation()
                This function actually creates the frame that the above macros sit in and calls each macro
                function so they can be built within the frame.
        """

        self.macroTitleBlock = ctk.CTkButton(self, text=' Macro Menu ', fg_color='black', font=('calibri BOLD', 20),
                                             width=50, height=25, border_width=2, anchor='w', hover=False,
                                             border_color="#f99d2a", text_color='white')
        self.macroTitleBlock.grid(row=1, column=0, sticky=ctk.W, padx=120)
        self.macroFrame = ctk.CTkFrame(self, width=325, height=370, border_width=2, fg_color='#4b6895', border_color="#f99d2a")
        self.macroFrame.grid_propagate(False)
        self.macroFrame.grid(row=2, column=0, columnspan=3, sticky=ctk.NW, padx=25, pady=10)
        self.macroFrame.grid_columnconfigure(3, weight=1)

        # Building of all lines within macro frame
        fastMove()
        layerMove()
        argonMacro()
        printingMacro()
        retractMacro()
        warmingMacro()
        outerWallMacro()
        innerWallMacro()
        fillMacro()
        saveAll()

    # ---------------------------------------

    # Macro command functions ---------------
    def fastMoveButton():
        """
            Name: fastMoveButton()
                Command functon for updating the fast move
        """

        commands.updateFastMove(self)

    def layerMoveButton():
        """
            Name: layerMoveButton()
                Command function for updating the layer move
        """

        commands.updateLayerMove(self)

    def argonButton():
        """
            Name: argonButton()
                Command function for updating the argon macro
        """

        commands.updateArgonMacro(self)

    def printingButton():
        """
            Name: printingButton()
                Command function for updating the printing macro
        """

        commands.updatePrintingMacro(self)

    def retractButton():
        """
            Name: retractButton()
                Command function for updating the retract macro
        """

        commands.updateRetractMacro(self)

    def warmingButton():
        """
            Name: warmingButton()
                Command function for updating the warming macro
        """

        commands.updateWarmingMacro(self)

    def outerWallButton():
        """
            Name: outerWallButton()
                Command function for updating the outer wall macro
        """

        commands.updateOuterWallMacro(self)

    def innerWallButton():
        """
            Name: innerWallButton()
                Command function for updating the inner wall macro
        """

        commands.updateInnerWallMacro(self)

    def fillButton():
        """
            Name: fillButton()
                Command function for updating the fill button
        """

        commands.updateFillMacro(self)

    def saveAllButton():
        """
            Name: saveAllButton()
                Command function for updating all macros
        """

        commands.updateAll(self)
    # ---------------------------------------

    macroFrameCreation()
