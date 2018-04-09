from Action import *
from MotorAction import *



class WaitForSpeechAction(Action):
    def __init__(self):
        super(WaitForSpeechAction, self).__init__()
        self.img = 'turn_body.gif'

        # Properties in format (GuiType, initialValue, min, max)

<<<<<<< HEAD
    def move_robot(self, args, controller):
        action = MotorAction()
        action.run_custom(controller, args[1], args[2])

=======
    def move_robot(self, args):
        # args is a list of arguments
        # eg move 5
        #                      5
>>>>>>> 7c7c35fba798fa4382498b391228acb3a65b4a80
        print("Moving Robot", args[0])

    def turn_robot(self, args):
        # eg. turn left 5
        #                       left     5
        print("Turning Robot", args[0], args[1])
        # or
        (direction, amount) = args
        print("Turning Robot", direction, amount)
<<<<<<< HEAD
    def run_now(self):
        print("running")
        return
=======
>>>>>>> 7c7c35fba798fa4382498b391228acb3a65b4a80

    # Override run function
    def run(self, controller, server):
        server.clients[0].text = "sst "

        while server.clients[0].command != "done":
            pass

        command = server.clients[0].command
        args = server.clients[0].args
<<<<<<< HEAD
        print(server.clients[0].command)
        if (server.clients[0].command == 'move'):
            self.move_robot(controller, args)
            print("in to move func")
        else:
            pass
=======

>>>>>>> 7c7c35fba798fa4382498b391228acb3a65b4a80
        server.clients[0].reset()

        {
            'move': self.move_robot,  # eg. move 5
            'turn': self.turn_robot,  # eg. turn left 5
            'exit': lambda e: exit(),
        }.get(command, lambda e: print('Invalid command'))(args)
<<<<<<< HEAD

        # args = server.run()


        #     return
=======
>>>>>>> 7c7c35fba798fa4382498b391228acb3a65b4a80

    def copy(self):
        return WaitForSpeechAction()
