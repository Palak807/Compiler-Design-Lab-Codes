import numpy as np


def checkGrammar(i):
    print("Enter the {} Production".format(str(i + 1)))
    input_grammar = list(input().split("->"))
    if input_grammar[0] == " " or input_grammar[0] == "" or input_grammar[0].islower() or len(input_grammar) == 1:
        return False
    else:
        input_grammar.pop(0)
        input_grammar = list(input_grammar[0])
        o = list("(abcdefghijklmnopqrstuvwxyz^/*+-|)")
        sp = ['!', '@', '#', '$', '?', '~', '`', ',', ';', ':', '"', '=', '_', '&', "'", "", " "]
        for i in range(0, len(input_grammar), 2):
            if input_grammar[i] == " ":
                result = False
            elif input_grammar[i] in sp:
                result = False
                break
            elif input_grammar[len(input_grammar) - 1] in o and (
                    (input_grammar[0] == "(" and input_grammar[len(input_grammar) - 1] == ")") or (
                    input_grammar.count("(") == input_grammar.count(")"))):
                result = True
            elif input_grammar[i].islower():
                result = True
            elif input_grammar[len(input_grammar) - 1] in o:
                result = False
            elif (i == len(input_grammar) - 1) and (input_grammar[i].isupper()):
                result = True
            elif (i == len(input_grammar) - 1) and (input_grammar[i].isupper() == False) and (input_grammar[i] in o) and \
                    input_grammar[i - 1] in o:
                result = True
            elif (input_grammar[i].isupper()) and (input_grammar[i + 1] in o):
                result = True
            elif (input_grammar[i].isupper()) and (input_grammar[i + 1].isupper()):
                result = False
                break
            else:
                result = False
                break
        if result is True:
            return True
        else:
            return False


def OPtable():
    operator = list(input(
        "Enter the operator used in the given grammar including the terminals and non-terminals"))
    operator.append('$')
    print(operator)
    o = list('(/*%+-)')
    table = np.empty([len(operator) + 1, len(operator) + 1], dtype=str, order="C")
    for j in range(1, len(operator) + 1):
        table[0][j] = operator[j - 1]
        table[j][0] = operator[j - 1]
    for _ in range(1, len(operator) + 1):
        for j in range(1, len(operator) + 1):
            if (table[_][0].islower()) and (table[0][j].islower()):
                table[_][j] = ""
            elif table[_][0].islower():
                table[_][j] = ">"
            elif (table[_][0] in o) and (table[0][j] in o):
                if o.index(table[_][0]) <= o.index(table[0][j]):
                    table[_][j] = ">"
                else:
                    table[_][j] = "<"
            elif (table[_][0] in o) and table[0][j].islower():
                table[_][j] = "<"
            elif table[_][0] == "$" and table[0][j] != "$":
                table[_][j] = "<"
            elif table[0][j] == "$" and table[_][0] != "$":
                table[_][j] = ">"
            else:
                break
    print("The Operator Precedence Relational Table for the given grammar is: \n")
    print(table)


var = int(input("Enter the Number of Variables\n"))
for i in range(var):
    if checkGrammar(i):
        print("YEYY!! Grammar is accepted")
        OPtable()
    else:
        print("Grammar is not accepted ")
        break
