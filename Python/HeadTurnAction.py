from Action import *


class HeadTurnAction(Action):
    def __init__(self):
        super(HeadTurnAction, self).__init__()
        self.img = 'head_turn.gif'

        # Properties in format (initialValue, min, max)
        self.properties['a'] = (GuiType.SLIDER, 0, 0, 0)

    # Override run function
    def run(self):
        pass

    def copy(self):
        return HeadTurnAction()
