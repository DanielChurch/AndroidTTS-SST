from Action import *


class SpeakAction(Action):
    def __init__(self):
        super(SpeakAction, self).__init__()
        self.img = 'turn_body.gif'

        # Properties in format (initialValue, min, max)
        self.properties['a'] = (GuiType.SLIDER, 0, 0, 0)

    # Override run function
    def run(self):
        pass

    def copy(self):
        return SpeakAction()
