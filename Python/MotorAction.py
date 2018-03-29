from Action import *


class MotorAction(Action):
    def __init__(self):
        super(MotorAction, self).__init__()
        self.img = 'motor.gif'

        # Properties in format (initialValue, min, max)
        self.properties['Speed'] = (GuiType.SLIDER, 0, 0, 3)
        self.properties['Direction'] = (GuiType.SLIDER, 0, 0, 0.1)

    # Override run function
    def run(self):
        pass

    def copy(self):
        return MotorAction()
