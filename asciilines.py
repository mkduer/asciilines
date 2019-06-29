#!/usr/bin/env python3

import sys


def define_specs(file: str) -> ((int, int), [str]):
    """
    read the file and grab the canvas dimensions and ascii commands
    :param: file: the file that contains the canvas specifications
    :return dimensions, ascii_commands: tuple of tuple canvas dimensions (integer width x integer height) 
                                        and a list of string ascii commands
    """
    with open(file, 'r') as file:
        ascii_commands = file.read().splitlines()
        canvas_dim = ascii_commands.pop(0).split(' ')

    height = ord(canvas_dim[0]) - 48
    width = ord(canvas_dim[1]) - 48

    return (height, width), ascii_commands


def init_canvas(dimensions: (int, int)) -> [[str]]:
    """ 
    initialize a canvas 
    :param: width: width of canvas
    :param: height: height of canvas
    """
    canvas = []
    height = dimensions[0]
    width = dimensions[1]

    if width < 1 or width > 9 or height < 1 or height > 9:
        raise ValueError("invalid dimensions for canvas")

    for i in range(height):
        row = ['.' for j in range(width)]
        canvas.append(row)
    return canvas


def print_ascii_canvas(canvas: [[str]]):
    """
    print ascii canvas
    :param: canvas: list of each row in the canvas
    """
    for row in canvas:
        print("".join(row))


def draw_ascii_lines(canvas: [[str]], dimensions: (int, int), cmd: [str]) -> [[str]]:
    """
    runs the command to draw ascii lines on the canvas
    :param: canvas: list of each row in the canvas
    :param: cmd: ascii command for drawing line
    """
    symbol, direction = cmd[0], cmd[3]
    length = ord(cmd[4]) - 48
    row_neg = False
    col_neg = False

    if len(cmd[1]) > 1:
        row_neg = True
        row = (ord(cmd[1][1]) - 48) * -1
    else:
        row = ord(cmd[1]) - 48

    if len(cmd[2]) > 1:
        col_neg = True
        col = (ord(cmd[2][1]) - 48) * -1
    else:
        col = ord(cmd[2]) - 48

    if direction == "v":
        # handle negative coordinates
        if col_neg:
            return canvas
        if row_neg:
            while row < 0:
                row += 1
                length -= 1

        # draw the ascii line
        if length > 0:
            for point in range(length):
                # draw within canvas dimensions
                if row + point > dimensions[0] - 1:
                    break
                canvas[row + point][col] = symbol
    else:
        # handle negative coordinates
        if row_neg:
            return canvas
        if col_neg:
            while col < 0:
                col += 1
                length -= 1

        # draw the ascii line
        if length > 0:
            for point in range(length):
                # draw within canvas dimensions
                if col + point > dimensions[1] - 1:
                    break
                canvas[row][col + point] = symbol

    return canvas


def grab_test_canvas(file: str) -> str:
    """
    compares canvas with expected result
    :param: canvas: list of each row in the canvas
    :param: file: the file that contains the canvas specifications
    """
    testfile = file[:-3] + 'out'

    with open(testfile, 'r') as file:
        test_canvas = file.read().splitlines()

    test_canvas = ["".join(row) for row in test_canvas]
    test_canvas = "\n".join(test_canvas)

    return test_canvas


def main(file: str):
    """ 
    main function that processes the specifications in the given file
    and uses the specs to print an ascii canvas 
    :param: file: the file that contains the canvas specifications
    """
    dimensions, ascii_commands = define_specs(file)
    canvas = init_canvas(dimensions)

    for cmd in ascii_commands:
        canvas = draw_ascii_lines(canvas, dimensions, cmd.split(" "))

    test_canvas = grab_test_canvas(file)

    canvas = ["".join(row) for row in canvas]
    canvas = "\n".join(canvas)

    if canvas != test_canvas:
        raise ValueError("the created canvas does not match the expected output")

    print(f'{canvas}')


def parse_args():
    """ parse command-line arguments and grab valid file or raise error """
    total_args = len(sys.argv)

    if 2 < total_args or total_args < 2:
        raise TypeError("incorrect number of arguments. EXAMPLE of correct usage: `./asciilines.py filename.tvg")

    file = sys.argv[1]
    if ".tvg" not in file:
        raise TypeError("WARNING: invalid file type. Expecting a .tvg file")

    return file


if __name__ == '__main__':
    filename = parse_args()
    main(filename)
