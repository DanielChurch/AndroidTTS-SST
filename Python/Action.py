from tkinter import *
from enum import Enum, auto


class GuiType(Enum):
    # (SLIDER, init val, min, max)
    SLIDER = auto()
    # (TEXTBOX, init text)
    TEXTBOX = auto()
    # (DROPDOWN, init index, [options])
    DROPDOWN = auto()


class Action:
    def __init__(self):
        self.img = ""
        # Unique map of properties in format (GuiType, initialValue, min, max)
        self.properties = {}

    def run(self):
        pass

    def copy(self):
        pass

    def getPropertyValue(self, property):
        return float(self.properties[property][0])

    # Lets us draw the image, we can't load in the image until tkinter is init
    def image(self):
        if type(self.img) is str:
            self.img = PhotoImage(file=self.img)
        return self.img
