from colorama import init, Fore, Back, Style
error = False
def print_error(string):
    global error
    print(Fore.RED + 'Error: ' + string + Style.RESET_ALL)
    error = True
def check_string(line):
    if line[0] == "\"" and line[-1] == "\"":
        return True
    else:
        return False
def to_string(value):
    return value.insert(0, "\"").insert(-1, "\"")

def force_exit():
    if error:
        exit(1)