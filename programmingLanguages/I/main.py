from operator import contains
from Util import *
import sys
from colorama import init, Fore, Back, Style
i = 0
def interpret(line):
    if line[-1] != ';':
        print_color("LINE " + str(i) + ": NO SEMICOLON", Fore.RED)
        sys.exit(1)
def main():
    args = sys.argv
    if len(args) > 2 or len(args) < 1 or args[1][0] != '-' and args[1][1] != '-':
        print_color("INVALID ARGUMENTS", Fore.RED)
        return
    else:
        filename = args[1].replace('-', '')
        global i
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                i += 1
                interpret(line.strip())
if __name__ == '__main__':
    main()