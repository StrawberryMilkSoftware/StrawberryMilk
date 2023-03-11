# Strawberry Milk Programming Language Interpreter Shell

import process
import sys
import smRpc

try:
    with open(sys.argv[1]) as f_in:
        lines = (line.rstrip() for line in f_in) 
        lines = list(line for line in lines if line) # Non-blank lines in a list
    for line in lines:
        res = process.processCmd(line)
        if res == "" or None:
            pass
        else:
            print(res)


        
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
            elif cmd == "ENABLE_BALLS":
                print("bruh")
            else:
                res = process.processCmd(cmd)
                if res == "" or None:
                    pass
                else:
                    print(res)