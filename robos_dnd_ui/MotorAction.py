from Action import *


class MotorAction(Action):
    def __init__(self):
        super(MotorAction, self).__init__()
        self.img = 'motor.gif'

        # Properties in format (initialValue, min, max)
        self.properties['Speed'] = (1, 1, 3)
        self.propertyList['Speed'] = {1, 2, 3}
        self.properties['Forward'] = (0, 0, 1)
        self.propertyList['Direction'] = (0, 1)
        self.properties['Duration'] = (0, 0, 10)
        self.properties['Rotate'] = (0, -1, 1)
    # Override run function
    def run(self, controller):
        speed = int(self.getPropertyValue('Speed'))
        direction = int(self.getPropertyValue('Forward'))
        duration = int(self.getPropertyValue('Duration'))
        rot = int(self.getPropertyValue('Rotate'))
        duration = int(self.getPropertyValue('Duration')/1000)
        if (rot == 1):
            controller.setAccel(2, 6)
            controller.setTarget(2, 5000)
         #   time.sleep(duration)
            
        elif(rot == -1):
            controller.setAccel(2, 6)
            controller.setTarget(2, 7000)
        #    time.sleep(duration)
        
	    
        if direction == 1:
            print("something")
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
        print(duration)
        time.sleep(duration)
        pass

    def copy(self):
        return MotorAction()
