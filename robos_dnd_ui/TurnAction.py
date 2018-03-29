from Action import *


class TurnAction(Action):
    def __init__(self):
        super(TurnAction, self).__init__()
        self.img = 'turn_body.gif'

        # Properties in format (initialValue, min, max)
        self.properties['Rotate (0 = left, 1 = right'] = (0, 0, 1)
        self.properties['Duration'] = (1000, 0, 10000)


    # Override run function
    def run(self, controller):
        duration = self.getPropertyValue('Duration')/1000
        if (self.getPropertyValue('Rotate (0 = left, 1 = right') == 1):
            controller.setAccel(2, 6)
            controller.setTarget(2, 5000)
            time.sleep(duration)
            pass
        else:
            controller.setAccel(2, 6)
            controller.setTarget(2, 7000)
            time.sleep(duration)
            pass

    def copy(self):
        return TurnAction()
