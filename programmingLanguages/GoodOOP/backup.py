from utils import *
variables = {}
functions = []
content = ""
for i in range(len(content)):
    line = content[i].replace("\t", "")
    if line[-1] != ";" and not line[0:8] == "function" and not line == "}":
        print_error("SEMICOLON MISSING!!!!")
        exit(1)
    if line[0:5] == "print":
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
        continue
    if line[0:3] == "var":
        variables[line[4:line.index("=") - 1].strip()] = line[line.index("=") + 2:line.index(";")]
        continue
    try:
        if line[0:line.index("=")].strip() in variables.keys():
            variables[line[0:line.index("=") - 1]] = line[line.index("=") + 2:line.index(";")]
            continue
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
            continue
    except:
        force_exit()
    if line[0:8] == "function":
        functions.append(line)
        continue
    try:
        if line.replace(";", "") in functions:
            continue
    except:
        force_exit()