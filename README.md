# asciilines

The first assignment in CS561 Open Source that turns .tvg input into a specified ascii output.

### Description
This program takes a text vector graphic (*.tvg*) file that specifies the canvas dimensions and what ascii is to be printed horizontally and/or vertically on the canvas. 

### Build and Run
This script was created with Python 3.7 (and should run on Python 3.6 or higher to allow for formatting of string literals e.g. `print(f'hello {var}')`). To build and run the script:

  * Clone the program:  
    `git clone git@github.com:mkduer/asciilines.git`.  

  * Go into the `asciilines` directory:  
    `cd asciilines`  

  * Make sure the permissions on the python script are correct:  
    `chmod 755 asciilines.py`  

  * Run the script with one of the provided .tvg test files in the `tests` directory:  
     `./asciilines tests/test1.tvg`  


### Testing, Bugs, Defects, etc.

Most of the error handling in this short program are dealt with by raising exceptions, as this seemed reasonable for the goals/expectations for this assignment.

##### ***file error handling***

TypeErrors are reaised if incorrect files or arguments are passed in. A ValueError is raised if a dimension less than zero is in the .tvg file. These checks are made in the `parse_args` function.

##### ***canvas parameters***

A ValueError is thrown in `init_canvas` if a dimension less than 1 is given by the .tvg file (as a canvas must at least consist of one row or one column).

##### ***canvas test***

Finally, a ValueError is raised in `main` if the resulting canvas does not match the expected canvas (example: from *test1.out*).

##### ***final notes***

Due to the small scope of this problem, I decided against running `pytest` or unit tests, and stuck with exception raising.. Additional tests that could be made would be checks for valid symbol processing, making limits on the canvas dimensions if desired, etc.


#### License

Copyright © 2019 Michelle Duer
Licensed under the "MIT License"
