from prettytable import PrettyTable


def first(string):
    firstValue = set()
    if string in nonTerminals:
        value = prodDict[string]

        for i in value:
            first2 = first(i)
            firstValue = firstValue | first2

    elif string in terminals:
        firstValue = {string}

    elif string == '' or string == 'ε':
        firstValue = {'ε'}

    else:
        first2 = first(string[0])
        if 'ε' in first2:
            i = 1
            while 'ε' in first2:
                firstValue = firstValue | (first2 - {'ε'})
                if string[i:] in terminals:
                    firstValue = firstValue | {string[i:]}
                    break
                elif string[i:] == '':
                    firstValue = firstValue | {'ε'}
                    break
                first2 = firstValue(string[i:])
                firstValue = firstValue | first2 - {'ε'}
                i += 1
        else:
            firstValue = firstValue | first2
    return firstValue


def follow(nonTer):
    followValue = set()
    prods = prodDict.items()
    if nonTer == startingSymbol:
        followValue = followValue | {'$'}
    for nt, rhs in prods:
        for alt in rhs:
            for char in alt:
                if char == nonTer:
                    nextChar = alt[alt.index(char) + 1:]
                    if nextChar == '':
                        if nt == nonTer:
                            continue
                        else:
                            followValue = followValue | follow(nt)
                    else:
                        follow2 = first(nextChar)
                        if 'ε' in follow2:
                            followValue = followValue | follow2 - {'ε'}
                            followValue = followValue | follow(nt)
                        else:
                            followValue = followValue | follow2
    return followValue


no_of_terminals = int(input("Enter the number of terminals: "))

terminals = []

print("Enter the terminal values :")
for _ in range(no_of_terminals):
    terminals.append(input())

no_of_non_terminals = int(input("Enter the number of non terminals: "))

nonTerminals = []

print("Enter the non terminal values :")
for _ in range(no_of_non_terminals):
    nonTerminals.append(input())

startingSymbol = input("Enter the starting symbol: ")

noProductions = int(input("Enter number of productions: "))

productions = []

print("Enter the productions:")
for _ in range(noProductions):
    productions.append(input())

prodDict = {}

for nT in nonTerminals:
    prodDict[nT] = []

for production in productions:
    NonTerminal = production.split("->")
    alternatives = NonTerminal[1].split("/")
    for alternative in alternatives:
        prodDict[NonTerminal[0]].append(alternative)

FIRST = {}
FOLLOW = {}

for nonTerminal in nonTerminals:
    FIRST[nonTerminal] = set()

for nonTerminal in nonTerminals:
    FOLLOW[nonTerminal] = set()

for nonTerminal in nonTerminals:
    FIRST[nonTerminal] = FIRST[nonTerminal] | first(nonTerminal)

FOLLOW[startingSymbol] = FOLLOW[startingSymbol] | {'$'}
for nonTerminal in nonTerminals:
    FOLLOW[nonTerminal] = FOLLOW[nonTerminal] | follow(nonTerminal)

valueTable = PrettyTable(['Non Terminals', 'First', 'Follow'])

for nonTerminal in nonTerminals:
    valueTable.add_row([nonTerminal, str(FIRST[nonTerminal]), str(FOLLOW[nonTerminal])])

print(valueTable)
