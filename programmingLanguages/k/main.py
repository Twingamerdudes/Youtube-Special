from os import system
import re
from colorama import init, Fore, Style
init()
TOKENS = ["print", "int", "string", "float", "var", "set", "input", "if", "else", "while"]
varNames = []
varValues = {}
varTypes = {}
code = 0
lineNumber = 0
#does code conatins a letter
def isLetter(char):
    if char.isalpha() or char == "_":
        return True
    else:
        return False
def print_error(string, **kwargs):
    print(f"{Style.NORMAL}{Fore.RED}{string}{Style.RESET_ALL}", **kwargs)

FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
def runProgram(programName):
    file = open(programName, "r")
    i = 0
    for line in file:
        if i == lineNumber:
            readCode(token(line))
            i += 1
def token(line):
    line = line.replace("\t", "")
    lineSplit = line.split(" ")
    tokenized = []
    for token in TOKENS:
        if line.startswith(token):
            tokenized.append(token)
    if "(" in lineSplit[0]:
        tokenized.append(line[line.index("(") + 1:-1])
        if "," in tokenized[1]:
            tokenized[1] = tokenized[1].split(",")
        for i in tokenized:
            for j in i:
                if j == ")":
                    temp = i[0:len(i) - 1]
                    tokenized.remove(i)
                    tokenized.append(temp)
        if "input" in lineSplit[0]:
            temp = tokenized[1]
            tokenized.remove(tokenized[1])
            tokenized.append(temp[0][1:-1])
            tokenized.append(temp[1][1:-1])
    if "var" in lineSplit[0]:
        if ":" in line and "<-" in line:
            tokenized.append(line[line.index("var") + 4:line.index(":")])
            tokenized.append(line[line.index(":") + 1:line.index("<") - 1])
            tokenized.append(line[line.index("<")+ 3:])
            varNames.append(tokenized[1])
    if "run" in lineSplit[0]:
        runProgram(line[line.index("run") + 4:])
        return "File ran"
    if "set" in lineSplit[0]:
        tokenized.append(line[4:line.index("<") - 1])
        tokenized.append(line[line.index("-") + 2:])
    if "if" in lineSplit[0]:
        if "==" in line:
            tokenized.append(line[line.index("if") + 3:line.index("==") - 1])
            tokenized.append(line[line.index("=="):line.index("==") + 2])
            tokenized.append(line[line.index("==") + 3:line.index("{")])
        print(tokenized)
    return tokenized
def readCode(line):
    global lineNumber
    lineNumber += 1
    if line[0] == "print":
        if "\"" in line[1]:
            print(line[1][1:-1])
        else:
            temp = line[1]
            if temp in varValues and varTypes[temp] == "string":
                value = varValues[temp].replace("\"", "").replace("\n", "").replace("\\n", "\n")
                print(value)
            elif temp in varValues:
                print_error("Var must be a string")
                exit(1)
            else:
                print_error("Var not found")
                exit(1)
    elif line[0] == "var":
        varValues[line[1]] = line[3]
        varTypes[line[1]] = line[2]
        if varTypes[line[1]] == "string" and "\"" not in line[3] or varTypes[line[1]] == "string" and line[3][len(line[3]) - 2] != "\"" or varTypes[line[1]] == "string" and line[3][0] != "\"":
            print_error("Line " + str(lineNumber) + ": String not surrounded by quotes")
            exit(1)
        elif varTypes[line[1]] != "string" and "\"" in line[3] or varTypes[line[1]] != "string" and line[3][len(line[3]) - 2] == "\"" or varTypes[line[1]] != "string" and line[3][0] == "\"":
            print_error("Line " + str(lineNumber) + ": Quotes not allowed in non-string variables")
            exit(1)
        elif varTypes[line[1]] == "float":
            for char in line[3]:
                if char.isalpha() and char != "f":
                    print_error("Line " + str(lineNumber) + ": Floats must only contain numbers (besides the f at the end)")
                    exit(1)
            if line[3][len(line[3]) - 2] != "f":
                print_error("Line " + str(lineNumber) + ": Floats must end in 'f'")
                exit(1)
            varValues[line[1]] = float(varValues[line[1]][0:len(line[1]) - 3])
        elif varTypes[line[1]] == "int":
            if re.search('[a-zA-Z]', line[3]):
                print_error("Line " + str(lineNumber) + ": Ints cannot have letters in them")
                exit(1)
            varValues[line[1]] = int(varValues[line[1]])
    elif line[0] == "set":
        if varTypes[line[1]] == "string" and "\"" not in line[2] or varTypes[line[1]] == "string" and line[2][len(line[2]) - 2] != "\"" or varTypes[line[1]] == "string" and line[2][0] != "\"":
            print_error("Line " + str(lineNumber) + ": String not surrounded by quotes")
            exit(1)
        if varTypes[line[1]] == "float":
            for char in line[2]:
                if char.isalpha() and char != "f":
                    print_error("Line " + str(lineNumber) + ": Floats must only contain numbers (besides the f at the end)")
                    exit(1)
            if line[2][len(line[2]) - 2] != "f":
                print_error("Line " + str(lineNumber) + ": Floats must end in 'f'")
                exit(1)
        if varTypes[line[1]] == "int" and re.search('[a-zA-Z]', line[2]):
            print_error("Line " + str(lineNumber) + ": Ints cannot have letters in them")
            exit(1)
        varValues[line[1]] = line[2]
    elif line[0] == "input":
        print(line[1], end="")
        varValues[line[2]] = "\"" + input() + "\""
    elif line[0] == "if":
        if line[2] == "==":
            global i
            if line[1] not in varNames and line[3] not in varNames:
                if line[1] == line[3]:
                    pass
                else:
                    #set i to the index of the } connected to the if statement
                    i = line.index("}")
            elif line[1] in varNames and line[3] in varNames:
                if varValues[line[1]].replace("\"", "") == varValues[line[3]].replace("\"", ""):
                    pass
                else:
                    pass
            elif line[1]in varNames and line[3] not in varNames:
                if varValues[line[1]].replace("\"", "") == line[3]:
                    pass
                else:
                    pass
            elif line[1] not in varNames and line[3] in varNames:
                if line[1] == varValues[line[3]].replace("\"", ""):
                    pass
                else:
                    pass
        else:
            print_error("Line " + str(lineNumber) + ": Invalid operator")
            exit(1)
print("> ", end="")
command = input()
tokened = token(command)
if tokened != "File ran":
    readCode(tokened)
else:
    print("\nProgram exited with code " + str(code))
system("pause")