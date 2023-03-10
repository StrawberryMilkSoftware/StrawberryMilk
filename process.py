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
sm_nullReference.errorDesc = "A function was not found for one of your commands."

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
    vars[varDescriptions[0]] = varDescriptions[1]
    return ""



def processCmd(cmd):
    result = ""

    try:
        if cmd == "":
            return ""
        elif "[c]" in cmd:
            return ""
        elif parseToFirstParen(cmd)[0] == "print":
            result = parsePrint(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "clear":
            result = clear()
        elif parseToFirstParen(cmd)[0] == "run":
            result = runFile(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "sys":
            result = systemRun(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "createPoint":
            result = createPoint(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "listPoints":
            result = listPoints()
        elif parseToFirstParen(cmd)[0] == "dvar":
            result = declareVar(parseToFirstParen(cmd)[1])
        else:
            result = sm_nullReference
    except:
        result = sm_parseError



    return result