from Action import *
import locale


class MotorAction(Action):
    def __init__(self):
        super(MotorAction, self).__init__()
        self.img = 'motor.gif'

        # Properties in format (initialValue, min, max)
        self.properties['Speed'] = (GuiType.SLIDER, 1, 1, 3)
        self.properties['Forward'] = (GuiType.SLIDER, 0, 0, 1)
        self.properties['Duration'] = (GuiType.SLIDER, 0, 0, 10)
        self.properties['Movement Direction'] = (GuiType.DROPDOWN, 'forward', ['forward', 'backward'])
        self.properties['Rotation Direction'] = (GuiType.DROPDOWN, 'left', ['left', 'right'])

    # Override run function
    def run(self, controller, server):
        speed = int(self.getPropertyValue('Speed'))
        direction = self.getPropertyValue('Movement Direction')
        rot = self.getPropertyValue('Rotation Direction')
        duration = int(self.getPropertyValue('Duration') / 1000)

        if rot == 'right':
            controller.setAccel(2, 6)
            controller.setTarget(2, 5000)
        else:
            controller.setAccel(2, 6)
            controller.setTarget(2, 7000)

        if direction == 'backward':
            if speed == 3:
                controller.setAccel(1, 1)
                controller.setTarget(1, 4000)
            elif speed == 2:
                controller.setAccel(1, 2)
                controller.setTarget(1, 4500)
            else:
                controller.setAccel(1, 1)
                controller.setTarget(1, 5000)
        else:
            if speed == 3:
                controller.setAccel(1, 3)
                controller.setTarget(1, 8000)
            elif speed == 2:
                controller.setAccel(1, 2)
                controller.setTarget(1, 7500)
            else:
                controller.setAccel(1, 1)
                controller.setTarget(1, 7000)
        time.sleep(duration)
        controller.setTarget(0, 6000)
        controller.setTarget(1, 6000)
        controller.setTarget(2, 6000)
        controller.setTarget(3, 6000)
        controller.setTarget(4, 6000)
        pass

    def run_custom(self, controller, dir, amount):
        # speed = int(self.getPropertyValue('Speed'))
        # direction = self.getPropertyValue('Forward')
        direction = dir
        locale.atof(amount)
        duration = float(amount)
        print("Moving" + " " + dir + " " + amount )

        if direction == 'right':
            controller.setAccel(2, 6)
            controller.setTarget(2, 5000)
        elif direction == 'left':
            controller.setAccel(2, 6)
            controller.setTarget(2, 7000)

        elif direction == 'backward':
            controller.setAccel(1, 1)
            controller.setTarget(1, 4000)

        else:
            controller.setAccel(1, 3)
            controller.setTarget(1, 8000)

        time.sleep(duration)
        pass
    def copy(self):
        return MotorAction()
