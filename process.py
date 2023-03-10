# Strawberry Milk Programming Language Command Processor

import os
import time

class point():
    pointName = "programStart"
    pointLine = 1

    def __repr__(self):
        return self.pointName

sm_programStart = point()
global points
points = [sm_programStart]

global vars
vars = {}


class error():
    errorName = "Undefined Error"
    errorDesc = "An undefined error has occurred"
    def __str__(self):
        return f"{self.errorName} \n {self.errorDesc}"

sm_syntaxError = error()
sm_syntaxError.errorName = "Syntax Error (sm_syntaxError)"
sm_syntaxError.errorDesc = "There is an error in the syntax of your code. Please check all syntax and try again."

sm_nullReference = error()
sm_nullReference.errorName = "Null Reference (sm_nullReference)"
sm_nullReference.errorDesc = "A reference was not found. (Function, variable, etc.)"

sm_parseError = error()
sm_parseError.errorName = "Parsing Error (sm_nullReference)"
sm_parseError.errorDesc = "There was an error while parsing one of your commands."

def parseToFirstParen(toParse):
    toParse = toParse.split("(")
    parsed1 = toParse[0]
    parsed2 = toParse[1]

    parsed = [parsed1, parsed2]

    return parsed


def parsePrint(toParse):

    if not ")" in toParse:
        return sm_parseError
    printString = toParse.replace(")", "")

    return printString

def parsePrintVar(toParse):

    if not ")" in toParse:
        return sm_parseError
    printString = toParse.replace(")", "")
    global vars
    try:
        printStringDone = vars[printString]
        return printStringDone
    except:
        return sm_nullReference
    

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def runFile(file):
    if not ")" in file:
        return sm_parseError
    file = file.replace(")", "")
    os.system(f"python3 smilk.py {file}")

def systemRun(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    os.system(cmd)

def parseCommas(toParse):
    p = toParse
    p = p.split(", ")
    return p

def createPoint(cmd):

    global points

    pointDescriptions = parseCommas(cmd)
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    newPoint = point()
    newPoint.pointName = pointDescriptions[0]
    newPoint.pointLine = pointDescriptions[1]
    points.append(newPoint)


def listPoints():
    global points
    return points

def declareVar(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")

    varDescriptions = parseCommas(cmd)
    global vars
    vars[varDescriptions[0]] = varDescriptions[1].replace(r"\n", "")

def getInput(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    inputDescriptions = parseCommas(cmd)
    global vars
    newVarName = inputDescriptions[1].replace("\n", "")

    vars[newVarName] = input(inputDescriptions[0])

def listVars():
    global vars
    return vars

def wait(stime):
    if not ")" in stime:
        return sm_parseError
    stime = stime.replace(")", "")
    stime = float(stime)

    time.sleep(stime)

def remVar(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    global vars
    try:
        del vars[cmd]
    except:
        return sm_nullReference

def combine(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    global vars

    varsToCombine = parseCommas(cmd)
    try:
        vars[varsToCombine[2]] = vars[varsToCombine[0]] + vars[varsToCombine[1]]
    except IndexError:
        return sm_syntaxError
    except:
        return sm_nullReference
    
def add(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    global vars

    varsToAdd = parseCommas(cmd)
    try:
        vars[varsToAdd[2]] = float(vars[varsToAdd[0]]) + float(vars[varsToAdd[1]])
    except IndexError:
        return sm_syntaxError
    except:
        return sm_nullReference

def sub(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    global vars

    varsToSub = parseCommas(cmd)
    try:
        vars[varsToSub[2]] = float(vars[varsToSub[0]]) - float(vars[varsToSub[1]])
    except IndexError:
        return sm_syntaxError
    except:
        return sm_nullReference

def mul(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    global vars

    varsToMul = parseCommas(cmd)
    try:
        vars[varsToMul[2]] = float(vars[varsToMul[0]]) * float(vars[varsToMul[1]])
    except IndexError:
        return sm_syntaxError
    except:
        return sm_nullReference
    
def div(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")
    global vars

    varsToDiv = parseCommas(cmd)
    try:
        vars[varsToDiv[2]] = float(vars[varsToDiv[0]]) / float(vars[varsToDiv[1]])
    except IndexError:
        return sm_syntaxError
    except:
        return sm_nullReference
    
def python(cmd):
    if not ")" in cmd:
        return sm_parseError
    cmd = cmd.replace(")", "")

    eval(cmd)


def processCmd(cmd):
    result = ""

    try:
        if cmd == "":
            return ""
        elif cmd == "\n":
            return ""
        elif cmd == None:
            return ""
        elif "[c]" in cmd:
            return ""
        elif parseToFirstParen(cmd)[0] == "print":
            result = parsePrint(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "clear":
            clear()
        elif parseToFirstParen(cmd)[0] == "run":
            result = runFile(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "sys":
            result = systemRun(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "createPoint":
            createPoint(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "listPoints":
            result = listPoints()
        elif parseToFirstParen(cmd)[0] == "var":
            declareVar(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "printvar":
            result = parsePrintVar(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "input":
            getInput(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "listVars":
            result = listVars()
        elif parseToFirstParen(cmd)[0] == "wait":
            wait(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "removeVar":
            remVar(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "combine":
            combine(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "add":
            add(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "sub":
            sub(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "mul":
            mul(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "div":
            div(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "python":
            python(parseToFirstParen(cmd)[1])
        else:
            result = sm_nullReference
    except:
        result = sm_parseError



    return result