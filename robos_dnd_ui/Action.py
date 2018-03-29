from tkinter import *
import time

from Maestro import Controller


class Action:
    def __init__(self):
        self.img = ""
        # Unique map of properties in format (initialValue, min, max)
        self.properties = {}
        self.propertyList = {}

    def getPropertyValue(self, property):
        return float(self.properties[property][0])

    def run(self, controller):
        pass

    def copy(self):
        pass

    # Lets us draw the image, we can't load in the image until tkinter is init
    def image(self):
        if type(self.img) is str:
            self.img = PhotoImage(file=self.img)
        return self.img
