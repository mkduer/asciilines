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


def draw_ascii_lines(canvas: [[str]], cmd: str) -> [[str]]:
    """
    runs the command to draw ascii lines on the canvas
    :param canvas: list of each row in the canvas
    :param cmd: ascii command for drawing line
    """
    symbol, direction = cmd[0], cmd[3]
    row = ord(cmd[1]) - 48
    col = ord(cmd[2]) - 48
    length = ord(cmd[4]) - 48

    start_coordinates = (row, col)

    # TODO: need to handle negative values for coordinates

    if direction == "v":
        end_coordinates = (row + length, col)
        for point in range(length):
            canvas[row + point][col] = symbol
    else:
        end_coordinates = (row, col + length)
        for point in range(length):
            canvas[row][col + point] = symbol

    return canvas


def canvas_test(filename: str, canvas: [[str]]) -> bool:
    """
    compares canvas with expected result
    :param canvas: list of each row in the canvas
    :param filename: the filename that contains the canvas specifications
    """
    testfile = filename[:-3] + 'out'

    with open(testfile, 'r') as file:
        test_canvas = file.read().splitlines()

    test_canvas = ["".join(row) for row in test_canvas]
    test_canvas = "\n".join(test_canvas)

    print(f'test canvas: \n{test_canvas}')  # TODO: delete test print

    canvas = ["".join(row) for row in canvas]
    canvas = "\n".join(canvas)

    print(f'canvas: \n{canvas}')  # TODO: delete test print
    return canvas == test_canvas


def main(filename: str):
    """ 
    main function that processes the specifications in the given file
    and uses the specs to print an ascii canvas 
    :param filename: the filename that contains the canvas specifications
    """
    dimensions, ascii_commands = define_specs(filename)
    canvas = init_canvas(dimensions)

    for cmd in ascii_commands:
        canvas = draw_ascii_lines(canvas, cmd.split(" "))

    if not canvas_test(filename, canvas):
        raise ValueError("the canvas does not contain the correct ascii values")

    print_ascii_canvas(canvas)


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
