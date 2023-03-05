# Strawberry Milk Programming Language Interpreter Shell

import process
import sys

try:
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    for line in lines:
        print(process.processCmd(line))
except IndexError:



    if __name__ == "__main__":
        print('''
     __  __ 
 ___|  \/  |
/ __| |\/| |
\__ \ |  | |
|___/_|  |_|
    ''')
        print("Strawberry Milk Programming Language Interpreter Shell")
        print("'quit' to quit")
        print("-==========-")

        while True:
            cmd = input("smilk >> ")
            if cmd == "quit":
                print("  Thanks for using sM!")
                exit()
            else:
                res = process.processCmd(cmd)
                print(res)
