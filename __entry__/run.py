import logging
import json

from _main_.parser import Parser


if __name__ == "__main__": 
    
    program = Parser('139dmasdjf')

    program.parse()

    print(program.Program())