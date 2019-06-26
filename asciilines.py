#!/usr/bin/env python3

import sys


def define_canvas_specs(filename: str) -> ((int, int), [str]):
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

    width = ord(canvas_dim[0]) - 48
    height = ord(canvas_dim[1]) - 48

    return (width, height), ascii_commands

def main(filename: str):
    """ 
    main function that processes the specifications in the file to print an ascii canvas 
    :param filename: the filename that contains the canvas specifications
    """
    print(f'filename: {filename}')

    canvas_dimensions, ascii_commands = define_canvas_specs(filename)
    print(f'canvas dimensions: {canvas_dimensions}')
    print(f'ascii cmds: {ascii_commands}')


    # TODO: function that creates canvas
    # TODO: function that runs commands (e.g. run through list of commands until end of list)
    # TODO: print resulting canvas
    # TODO: compare the result with the .out file result (manual diff or function)


def parse_args():
    """ parse command-line arguments and grab valid file or raise error """
    total_args = len(sys.argv)

    if 2 < total_args or total_args < 2:
        raise TypeError("WARNING: incorrect number of arguments. EXAMPLE of correct usage: `./asciilines.py filename.tvg")

    filename = sys.argv[1]
    if ".tvg" not in filename:
        raise TypeError("WARNING: invalid file type. Expecting a .tvg file")

    return filename


if __name__ == '__main__':
    filename = parse_args()
    main(filename)
