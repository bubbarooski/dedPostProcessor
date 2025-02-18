"""
    This file contains all piece of the frame housing the logo and title.
        IMPORTS:
            customtkinter
            PIL.Image
        FUNCTIONS:
            snowbirdLogoFrame
"""

import customtkinter as ctk
from PIL import Image


def snowbirdLogoFrame(self):
    """
        Name: snowbirdLogoFrame()
            This function creates the frame housing the logo and title.
        :param self: the app as a whole
    """

    # Logo frame ----------------------------
    logo = ctk.CTkImage(Image.open(".\images\logo.png"), size=(226, 75))
    self.logo = ctk.CTkButton(self, text='  Example Post Processor  ', font=('calibri BOLD', 24), image=logo,
                              fg_color='#000000', hover=False, height=80, width=250, border_width=2,
                              border_color="#f99d2a", text_color='white')
    self.logo.grid(row=0, column=0, sticky=ctk.W, pady=10, padx=25)
    self.logoDivider = ctk.CTkFrame(self, width=2, height=50, fg_color='white')
    self.logoDivider.grid(row=0, column=0, sticky=ctk.W, padx=265, pady=10)
    # ---------------------------------------
