from Action import *


class WaitForSpeechAction(Action):
    def __init__(self):
        super(WaitForSpeechAction, self).__init__()
        self.img = 'turn_body.gif'

        # Properties in format (GuiType, initialValue, min, max)
        self.properties[''] = (GuiType.SLIDER, 0, 0, 0)

    # Override run function
    def run(self):
        pass

    def copy(self):
        return WaitForSpeechAction()
