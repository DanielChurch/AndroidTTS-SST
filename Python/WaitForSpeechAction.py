from Action import *


class WaitForSpeechAction(Action):
    def __init__(self):
        super(WaitForSpeechAction, self).__init__()
        self.img = 'turn_body.gif'

        # Properties in format (GuiType, initialValue, min, max)

    def move_robot(self, args):
        # args is a list of arguments
        # eg move 5
        #                      5
        print("Moving Robot", args[0])

    def turn_robot(self, args):
        # eg. turn left 5
        #                       left     5
        print("Turning Robot", args[0], args[1])
        # or
        (direction, amount) = args
        print("Turning Robot", direction, amount)

    # Override run function
    def run(self, controller, server):
        server.clients[0].text = "sst "

        while server.clients[0].command != "done":
            pass

        command = server.clients[0].command
        args = server.clients[0].args

        server.clients[0].reset()

        {
            'move': self.move_robot,  # eg. move 5
            'turn': self.turn_robot,  # eg. turn left 5
            'exit': lambda e: exit(),
        }.get(command, lambda e: print('Invalid command'))(args)

    def copy(self):
        return WaitForSpeechAction()
