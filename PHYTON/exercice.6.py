# whatis.py

import sys

def check_number(num):
    try:
        num = int(num)
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("Argument is not an integer")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise AssertionError("More than one argument is provided")
    else:
        check_number(sys.argv[1])
