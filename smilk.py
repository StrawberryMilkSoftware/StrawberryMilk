# Strawberry Milk Programming Language Interpreter Shell

import process
import sys
import smRpc

try:
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    for line in lines:
        print(process.processCmd(line), end="")
except IndexError:



    if __name__ == "__main__":
        print('''
     __  __ 
 ___|  \/  |
/ __| |\/| | Strawberry Milk
\__ \ |  | | Programming Language
|___/_|  |_|
    ''')
        print("Interpreter Shell - - Pre-Alpha")
        print("'quit' to quit")
        print("-==========-")

        while True:
            cmd = input("smilk >> ")
            if cmd == "quit":
                print("Thanks for using sM!")
                exit()
            elif cmd == "enablerpc":
                print("Thanks to Saturn.py#0001")
                smRpc.enable()
            else:
                res = process.processCmd(cmd)
                print(res, end="")
