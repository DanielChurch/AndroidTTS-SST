from Action import *


class HeadTiltAction(Action):
    def __init__(self):
        super(HeadTiltAction, self).__init__()
        self.img = 'head_tilt.gif'

        # Properties in format (initialValue, min, max)
        self.properties['a'] = (GuiType.SLIDER, 0, 0, 0)

    # Override run function
    def run(self):
        pass

    def copy(self):
        return HeadTiltAction()
