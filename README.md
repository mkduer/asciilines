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

This program will raise an TypeErrors if incorrect files or arguments are passed in. It will also raise a ValueError if a dimension less than zero is in the .tvg file.

[ ] Information about bugs, defects, failing tests, etc  



#### License

Copyright © 2019 Michelle Duer
Licensed under the "MIT License"
