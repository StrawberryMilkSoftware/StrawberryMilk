#!/usr/bin/python3
# Strawberry Milk Programming Language Interpreter Shell

import process
import sys

try:
    if sys.argv[1].endswith(".sm") or sys.argv[1].endswith(".strawberrymilk") or sys.argv[1].endswith(".smilk"):
        with open(sys.argv[1]) as f_in:
            lines = (line.rstrip() for line in f_in) 
            lines = list(line for line in lines if line) # Non-blank lines in a list
        for line in lines:
            res = process.processCmd(line)
            if res == "" or None:
                pass
            else:
                print(res)
    else:
        print("This is not a strawberryMilk file type!")


        
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
            elif cmd == "ENABLE_BALLS":
                print("bruh")
            else:
                res = process.processCmd(cmd)
                if res == "" or None:
                    pass
                else:
                    print(res)

except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")