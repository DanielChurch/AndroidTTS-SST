import time
from Action import *


class PauseAction(Action):
    def __init__(self):
        super(PauseAction, self).__init__()
        self.img = 'timer.gif'

        # Properties in format (initialValue, min, max)
        self.properties['Duration'] = (GuiType.SLIDER, 5, 0, 10)

    # Override run function
    def run(self):
        print('timer start - running for', Action.getPropertyValue(self, 'Duration'), 'seconds')
        time.sleep(Action.getPropertyValue(self, 'Duration'))
        print('timer end')

    def copy(self):
        return PauseAction()
