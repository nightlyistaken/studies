## Python Basics
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

To get started with Python, install python from [here](https://www.python.org/downloads/).

### Hello World
Create a file called `hello.py`, and write the following code in it.
```py
# Prints the string "Hello World" to the console
print("Hello World")
```
To run the code, open a terminal in the same directory as the file, and run the following command.
```sh
python3 hello.py
```
### Comments
```py
# This is a comment. It is not executed by the python interpreter.
# Comments are used to explain the code, and to make it more readable.
print("You can use # to comment out a line of code")
print("You can use """ to comment out multiple lines of code")
"""
This wont be executed!
"""

```
### Strings
```py
# This is a string. It is surrounded by either single quotation marks, or double quotation marks.
my_string = "Hello World"
```
String literals in python are surrounded by either single quotation marks, or double quotation marks.
Strings are used to store text.
For example here we are printing the string `"Hello World"` to the console.

### Variables
```py
# A variable is a container for a value, which can be of various types. Kind of like in maths, where x = 5 means that x is equal to 5.
x = 5 
y = "John" 
print(x) 
print(y) 
```
In the above example, we are creating two variables, `x` and `y`. `x` is an integer variable, and `y` is a string variable. We are then printing the variables to the console.

Python uses indentation to define blocks of code. This means that you use whitespace (usually 4 spaces) to indicate where a block of code begins and ends.

Example:
```py
def main():
    print("This code is inside this function")
print("This code is outside the function")
```