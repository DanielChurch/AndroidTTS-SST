from Action import *


class SpeakAction(Action):
    def __init__(self):
        super(SpeakAction, self).__init__()
        self.img = 'turn_body.gif'

        # Properties in format (initialValue, min, max)
        self.properties['Presets'] = (GuiType.DROPDOWN, 'Hello World',
                                      ['Hello World',
                                       'Get down he has a gun! @@@@@@@@@@@@@@@@@@@@',
                                       '',
                                       '',
                                       ''
                                       ])
        self.properties['Custom Quote'] = (GuiType.TEXTBOX, '')

    # Override run function
    def run(self, controller):
        if len(self.getPropertyValue('Custom Quote')) == 0:
            # Use custom
            pass
        else:
            # Use Preset
            pass

    def copy(self):
        return SpeakAction()
