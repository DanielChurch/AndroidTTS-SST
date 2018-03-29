from Action import *


class BodyTurnAction(Action):
    def __init__(self):
        super(BodyTurnAction, self).__init__()
        self.img = 'turn_body.gif'

        self.properties['a'] = (GuiType.SLIDER, 0, 0, 0)
        self.properties['b'] = (GuiType.TEXTBOX, 'how now brown cow')
        self.properties['c'] = (GuiType.SLIDER, 0, 0, 0)
        self.properties['d'] = (GuiType.DROPDOWN, 'one', ['one', 'two', 'three'])

    # Override run function
    def run(self):
        pass

    def copy(self):
        return BodyTurnAction()
