
import sys
from antlr4 import *
from antlr.deLexer import deLexer as Lexer
from antlr.deParser import deParser as Parser
from runVisitor import runVisitor as Visitor


def main(argv):
    input = FileStream(argv[1])

    #input =InputStream("""log "this is test" """)

    #input =InputStream("""x = 4; """)

    #print input

    lexer = Lexer(input)
    stream = CommonTokenStream(lexer)
    try:
        parser = Parser(stream)
        #print "parser"
        #print parser
    except:
        print "something wroing with parser"
    tree = parser.parse()
    #print "tree"
    #print tree
    visitor = Visitor()
    #print "visitor"
    #print visitor
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
