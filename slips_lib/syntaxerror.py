from lib2to3.pgen2.tokenize import generate_tokens, TokenError
from lib2to3.pgen2.driver import Driver
from lib2to3.pgen2.parse import ParseError
from lib2to3.pygram import python_grammar_no_print_statement
from lib2to3.pytree import convert as convert_tree
import logging
import itertools

import argparse

argparser = argparse.ArgumentParser(description='Retrieve a source file for parsing.')
argparser.add_argument('file', type=str, help='path to file')
args = argparser.parse_args()


driver = Driver(python_grammar_no_print_statement,
                convert=convert_tree)
                
                
with open(args.file) as f:

    def readline():
        while True:
            line = f.readline()
            
            if line.endswith('\n'):
                yield line
            else:
                yield line+'\n'
                yield ''
                break

    tokens, tokens_copy = itertools.tee(generate_tokens(readline().__next__))
    
    try:
        st = driver.parse_tokens(tokens)
        print(st)

    except TokenError as err:
        print([t for t in tokens_copy])
        
    except IndentationError as err:
        print(err.msg)
        print(err.filename)
        print(err.lineno)
        print(err.offset)
        print(err.text)
        
    except ParseError as err:
        print(err.msg)
        print(err.type)
        print(err.value)
        print(err.context)