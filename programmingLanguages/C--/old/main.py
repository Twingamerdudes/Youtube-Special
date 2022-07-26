import sys, shlex

ignore = ["#include", "void"]
strings = []
stringNames = []
def lexer(y):
    return shlex.split(y)
def main():
    file = open("test.sc", "r")
    content = file.read().split("\n")
    for line in content:
        if line != "":
            if line[-1] != ";" and lexer(line)[0] not in ignore:
                print("ERROR")
                sys.exit(1)
            parser(lexer(line.split(".")))
def parser(lexed):
    if lexed[0] == "string":
        try:
            strings.append(lexed[3])
            if lexed[2] != "=":
                print("ERROR")
                sys.exit()
            stringNames.append(lexed[1])
        except:
            stringNames.append(lexed[1])
    if lexed[0] == "Console":
        if lexed[1] == "printf":
            pass
if __name__ == "__main__":
    main()