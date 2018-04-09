from Action import *
from MotorAction import *



class WaitForSpeechAction(Action):
    def __init__(self):
        super(WaitForSpeechAction, self).__init__()
        self.img = 'stt.gif'

        # Properties in format (GuiType, initialValue, min, max)


    def move_robot(self, controller, args):
        action = MotorAction()
        print("Moving")
        action.run_custom(controller, args[0], args[1])

        print("Moving Robot" + args[0])

    def turn_robot(self, args):
        # eg. turn left 5
        #                       left     5
        print("Turning Robot", args[0], args[1])
        # or
        (direction, amount) = args
        print("Turning Robot", direction, amount)
    def run_now(self):
        print("running")
        return

    def run_now(self):
        print("running")
        return

    # Override run function
    def run(self, controller, server):
        server.clients[0].text = "sst "
        print(server.clients[0].command)
        while (server.clients[0].command != "start" and server.clients[0].command != 'continue'):
            command = server.clients[0].command
            args = server.clients[0].args


            if (command == 'move'):
                self.move_robot(controller, args)
                print("in to move func")
                return
            else:
                pass

        server.clients[0].reset()

        {
            'move': self.move_robot,  # eg. move 5
            'turn': self.turn_robot,  # eg. turn left 5
            'exit': lambda e: exit(),
        }.get(command, lambda e: print('Invalid command'))(args)



    def copy(self):
        return WaitForSpeechAction()
