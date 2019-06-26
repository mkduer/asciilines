#!/usr/bin/env python3

import sys


def define_specs(filename: str) -> ((int, int), [str]):
    """
    read the file and grab the canvas dimensions and ascii commands
    :param filename: the filename that contains the canvas specifications
    :return dimensions, ascii_commands: tuple of tuple canvas dimensions (integer width x integer height) 
                                        and a list of string ascii commands
    """
    width, height = 0, 0
    ascii_commands = []
    canvas_dim = ""

    with open(filename, 'r') as file:
        ascii_commands = file.read().splitlines()
        canvas_dim = ascii_commands.pop(0).split(' ')

    height = ord(canvas_dim[0]) - 48
    width = ord(canvas_dim[1]) - 48

    return (height, width), ascii_commands

def init_canvas(dimensions: (int, int)) -> [[str]]:
    """ 
    initialize a canvas 
    :param width: width of canvas
    :param height: height of canvas
    """
    canvas = []
    height = dimensions[0]
    width = dimensions[1]

    if width == 0 or height == 0:
        raise ValueError("invalid dimensions for canvas")

    for i in range(height):
        row = ['.' for j in range(width)]
        canvas.append(row)
    return canvas


def print_ascii_canvas(canvas: [[str]]):
    """
    print ascii canvas
    :param canvas: list of each row in the canvas
    """
    for row in canvas:
        print("".join(row))


def draw_ascii_lines(canvas: [[str]], cmd: str):
    """
    runs the command to draw ascii lines on the canvas
    :param canvas: list of each row in the canvas
    :param cmd: ascii command for drawing line
    """
    canvas[2][1] = "&"
    return canvas


def main(filename: str):
    """ 
    main function that processes the specifications in the file to print an ascii canvas 
    :param filename: the filename that contains the canvas specifications
    """
    dimensions, ascii_commands = define_specs(filename)
    print(f'dimensions: {dimensions}')
    print(f'ascii cmds:')
    for cmd in ascii_commands:
        print(f'{cmd}')

    canvas = init_canvas(dimensions)
    print(f'init canvas:')
    print_ascii_canvas(canvas)  # TODO test print delete

    # TODO: function that runs commands (e.g. run through list of commands until end of list)
    canvas = draw_ascii_lines(canvas, ascii_commands[0])
    print(f'modified canvas:')
    print_ascii_canvas(canvas)  # TODO test print delete

    # TODO: print resulting canvas
    # TODO: compare the result with the .out file result (manual diff or function)


def parse_args():
    """ parse command-line arguments and grab valid file or raise error """
    total_args = len(sys.argv)

    if 2 < total_args or total_args < 2:
        raise TypeError("incorrect number of arguments. EXAMPLE of correct usage: `./asciilines.py filename.tvg")

    filename = sys.argv[1]
    if ".tvg" not in filename:
        raise TypeError("WARNING: invalid file type. Expecting a .tvg file")

    return filename


if __name__ == '__main__':
    filename = parse_args()
    main(filename)
