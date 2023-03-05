# Strawberry Milk Programming Language Command Processor

import os


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


def processCmd(cmd):
    result = ""

    try:
        if cmd == "":
            return ""
        elif parseToFirstParen(cmd)[0] == "print":
            result = parsePrint(parseToFirstParen(cmd)[1])
        elif parseToFirstParen(cmd)[0] == "clear":
            clear()
        elif parseToFirstParen(cmd)[0] == "run":
            runFile(parseToFirstParen(cmd)[1])
        else:
            result = sm_nullReference
    except:
        result = sm_parseError



    return result