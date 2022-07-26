from tabnanny import check
from telnetlib import LINEMODE
from utils import *
variables = {}
functions = []
print("File: ", end="")
fileName = input()
file = open(fileName, "r")
content = file.read().split("\n")
file.close()
def interpet(content):
    line = content[i].replace("\t", "")
    if line[-1] != ";" and not line[0:8] == "function" and not line == "}":
        print_error("SEMICOLON MISSING!!!!")
        exit(1)
    if line[0:5] == "print" and "()" not in line:
        if not check_string(line[6:line.index(";")]):
            if line.replace("\"", "")[6:line.index(";")] in variables.keys():
                var = variables[line.replace("\"", "")[6:line.index(";")]]
                if(check_string(var)):
                    print(var.replace("\"", ""))
                else:
                    print_error("INVALID STRING")
                    exit(1)  
            else:
                print_error("INVALID STRING OR UNDECLARED VARAIBLE!!!!!")
                exit(1)
        else:
            line = line.replace("\"", "")
            print(line[6:line.index(";")])
        return
    if line[0:3] == "var":
        variables[line[4:line.index("=") - 1].strip()] = line[line.index("=") + 2:line.index(";")]
        return
    try:
        if line[0:line.index("=")].strip() in variables.keys():
            variables[line[0:line.index("=") - 1]] = line[line.index("=") + 2:line.index(";")]
            return
    except:
        force_exit()
    try:
        if line[0:line.index(".")].strip() in variables.keys():
            var = variables[line[0:line.index(".")].strip()]
            if "insert" in line[line.index("."):] and check_string(var):
                parms = line[line.index("insert") + 7:line.index(";")].split(",")
                if parms == ['']:
                    print_error("INVALID FUNCTION PARAMETERS")
                    exit(1)
                if len(parms) == 2 and check_string(parms[1].strip()) and not check_string(parms[0].strip()):
                    var = var.replace("\"", "")
                    var = var[:int(parms[0].strip())] + parms[1].strip().replace("\"", "") + var[int(parms[0].strip()):]
                    var = "\"" + var + "\""
                    variables[line[0:line.index(".")].strip()] = var
                else:
                    print_error("INVALID FUNCTION PARAMETERS")
                    exit(1)
            elif "remove" in line[line.index("."):] and check_string(var):
                parms = line[line.index("remove") + 7:line.index(";")]
                if parms == "":
                    print_error("INVALID FUNCTION PARAMETERS")
                    exit(1)
                if check_string(parms.strip()):
                    var = var.replace("\"", "")
                    index = var.index(parms.strip().replace("\"", ""))
                    var = var[:index] + var[index + len(parms.strip().replace("\"", "")):]
                    variables[line[0:line.index(".")].strip()] = "\"" + var + "\""
                else:
                    print_error("INVALID FUNCTION PARAMETERS")
                    exit(1)
            else:
                print_error("INVALID FUNCTION")
                exit(1)
            return
    except:
        force_exit()
    if line[0:8] == "function":
        functions.append(line[9:line.index("(")].strip())
        return
    try:
        print(line[0:line.index("(")] + " " + str(functions))
        if line[0:line.index("(")] in str(functions):
            print("test")
            interpet(content[i + 1:content.index("}")])
            return
    except:
        force_exit()
for i in range(len(content)):
    interpet(content)