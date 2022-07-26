from colorama import init, Fore, Back, Style
import sys
def print_color(text, color):
    print(color + text + Style.RESET_ALL)
def clear():
    print("\033[H\033[J", end="")
    sys.stdout.flush()