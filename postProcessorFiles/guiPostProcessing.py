"""
    This file is used for post-processing directly related to the GUI. The post process file still exists,
    but this is used to show the potential processed code as well as write it to the frame.
        IMPORTS:
            postProcessorFiles.postProcess.file
            postProcessorFiles.postProcess.postProcessingControlFunction
            Config.parse.parseConfig
            tkinter.filedialog
        FUNCTIONS:
            guiPostProcess()
            guiWriteNewFile()
"""

from postProcessorFiles.postProcess import file, postProcessingControlFunction
from Config.parse import parseConfig
from tkinter import filedialog


def guiPostProcess(filename):
    """
        Name: guiPostProcess()
            This function is used to post process a selected file and return the post processed lines.
            This is called from the GUI, hence why a name of 'test' and file number of 1234 is used,
            and will not be written in its current form.
        :param filename: the name of the file being post processed
        :return: lines: a list of the lines post processed
    """

    parameters = parseConfig()
    fileObject = file(filename, str(1234), 'test', parameters.get('layerWait'), parameters.get('fastWait'))
    lines = postProcessingControlFunction(fileObject, 1)
    return lines


def guiWriteNewFile(self):
    """
        Name: guiWriteNewFile()
            This function is used to write a post processed file chosen in the GUI. It allows a user to
            input a filename and grabs the file number before exporting the post processed file.
        :param self: the GUI
    """

    # print(self.filename)
    self.exportName = filedialog.asksaveasfilename(initialdir="./Gcode/", title="Save exported filename",
                                                   filetypes=(("NC File", "*.nc*"), ("all files", "*.*")))

    if self.exportName[-3:] == ".nc":
        self.exportName = self.exportName[:-3]

    exportedFileDirectory = self.exportName + ".nc"
    openedFile = open(exportedFileDirectory, 'w')

    user = self.userEntry.get()
    version = '2.3.0'

    counter = 0
    openedFile.write(self.fileNumber + "\n")
    openedFile.write('N1 ' + '(USER: ' + user + ')\n')
    openedFile.write('N2 ' + '(VERSION: ' + version + ')\n')
    for line in self.lines:
        counter += 1
        openedFile.write(" ".join(line) + "\n")
    openedFile.close()
