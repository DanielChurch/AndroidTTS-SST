from sys import exit
import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6969

ss.bind(('25.14.181.224', port))
ss.listen(5)


def move_robot(args):
    # args is a list of arguments
    # eg move 5
    #                      5
    print("Moving Robot", args[0])


def turn_robot(args):
    # eg. turn left 5
    #                       left     5
    print("Turning Robot", args[0], args[1])
    # or
    (direction, amount) = args
    print("Turning Robot", direction, amount)


def on_sst(args):
    text = args[0]


while True:
    connection, address = ss.accept()

    print('yo dawg someone connected')

    command, *args = connection.recv(1024).decode('ascii').split(' ')

    print(command, args)

    {
        'move': move_robot,  # eg. move 5
        'turn': turn_robot,  # eg. turn left 5
        'sttResult': on_sst,
        'exit': lambda e: exit(),
    }.get(command, lambda e: print('Invalid command'))(args)

    connection.close()
