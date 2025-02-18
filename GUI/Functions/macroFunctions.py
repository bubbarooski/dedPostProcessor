"""
    This file houses functions that call the set macro function. Each function does a little
    checking to make sure that a valid entry is there and if so, calls the set function for
    that macro.
        IMPORTS:
            Config.macroSet
            postProcessorFiles.postProcess.codes
        FUNCTIONS:
            updateFastMove()
            updateLayerMove()
            updateArgonMacro()
            updatePrintingMacro()
            updateRetractMacro()
            updateWarmingMacro()
            updateOuterWallMacro()
            updateInnerWallMacro()
            updateFillMacro()
            updateAll()
"""

from Config import macroSet
from postProcessorFiles.postProcess import codes

codeList = codes()


def updateFastMove(app):
    """
        Name: updateFastMove()
            This function is used to call the setter for the fast move.
        :param app: the entire gui app
    """

    entry = app.fastMoveEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setFast(entry)


def updateLayerMove(app):
    """
        Name: updateLayerMove()
            This function is used to call the setter for the layer move.
        :param app: the entire gui app
    """

    entry = app.layerMoveEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setLayer(entry)


def updateArgonMacro(app):
    """
        Name: updateArgonMacro()
            This function is used to call the setter for the argon macro.
        :param app: the entire gui app
    """

    entry = app.argonEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setArgon(entry)


def updatePrintingMacro(app):
    """
        Name: updatePrintingMacro()
            This function is used to call the setter for the printing macro.
        :param app: the entire gui app
    """

    entry = app.printingEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setPrinting(entry)


def updateRetractMacro(app):
    """
        Name: updateRetractMacro()
            This function is used to call the setter for the retract macro.
        :param app: the entire gui app
    """

    entry = app.retractEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setRetract(entry)


def updateWarmingMacro(app):
    """
        Name: updateWarmingMacro()
            This function is used to call the setter for the warming macro.
        :param app: the entire gui app
    """

    entry = app.warmingEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setWarming(entry)


def updateOuterWallMacro(app):
    """
        Name: updateOuterWallMacro()
            This function is used to call the setter for the outer wall macro.
        :param app: the entire gui app
    """

    entry = app.outerWallEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setOuter(entry)


def updateInnerWallMacro(app):
    """
        Name: updateInnerWallMacro()
            This function is used to call the setter for the inner wall macro.
        :param app: the entire gui app
    """

    entry = app.innerWallEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setInner(entry)


def updateFillMacro(app):
    """
        Name: updateFillMacro()
            This function is used to call the setter for the fill macro.
        :param app: the entire gui app
    """

    entry = app.fillEntry.get()
    if not entry:
        print('nothing')
    else:
        macroSet.setFill(entry)


def updateAll(app):
    """
        Name: updateAll()
            This function is used to call the setter for all macros.
        :param app: the entire gui app
    """

    fastMove = app.fastMoveEntry.get()
    layerMove = app.layerMoveEntry.get()
    argon = app.argonEntry.get()
    printing = app.printingEntry.get()
    retract = app.retractEntry.get()
    warming = app.warmingEntry.get()
    outer = app.outerWallEntry.get()
    inner = app.innerWallEntry.get()
    fill = app.fillEntry.get()

    if fastMove == '':
        fastMove = str(1)
    if layerMove == '':
        layerMove = str(1)

    macroSet.setFast(fastMove)
    macroSet.setLayer(layerMove)
    macroSet.setArgon(argon)
    macroSet.setPrinting(printing)
    macroSet.setRetract(retract)
    macroSet.setWarming(warming)
    macroSet.setOuter(outer)
    macroSet.setInner(inner)
    macroSet.setFill(fill)
