from tkinter import *

windowWidth = 250
windowHeight = 360


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


class PropertyEditor:
    def __init__(self, action):
        master = Toplevel()

        self.scales = []
        for i in range(len(action.properties.keys())):
            key = list(action.properties.keys())[i]
            value, start, end = action.properties[key]

            def onScroll(val):
                keys = list(action.properties.keys())
                for n in range(len(self.scales)):
                    action.properties[keys[n]] = (self.scales[n].get(), action.properties[keys[n]][1], action.properties[keys[n]][2])
            self.scales.append(Scale(master, label=str(key), from_=start, to=end, resolution=1.0, orient=HORIZONTAL, command=onScroll))
            self.scales[-1].grid(row=i, column=0, sticky='ew', columnspan=2)
            self.scales[-1].set(value)

        Frame(master, width=windowWidth, height=windowHeight, bd=2, relief=GROOVE)
        center(master)
