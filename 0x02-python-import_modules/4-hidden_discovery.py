#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for printname in dir(hidden_4):
        if printname[0] != "_":
            print(printname)
