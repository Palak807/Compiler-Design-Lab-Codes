def first(string):
    first1 = set()
    if string in nonTerminals:
        alter = productionDict[string]
        for i in alter:
            first2 = first(i)
            first1 = first1 | first2
    elif string in terminals:
        first1 = {string}
    elif string == '' or string == 'ε':
        first1 = {'ε'}
    else:
        first2 = first(string[0])
        if 'ε' in first2:
            i = 1
            while 'ε' in first2:
                first1 = first1 | (first2 - {'ε'})
                if string[i:] in terminals:
                    first1 = first1 | {string[i:]}
                    break
                elif string[i:] == '':
                    first1 = first1 | {'ε'}
                    break
                first2 = first(string[i:])
                first1 = first1 | first2 - {'ε'}
                i += 1
        else:
            first1 = first1 | first2
    return first1


numberTerminals = int(input("Enter no. of terminals: "))
terminals = []
print("Enter the terminals :")
for _ in range(numberTerminals):
    terminals.append(input())

numberNonTerminals = int(input("Enter no. of non terminals: "))
nonTerminals = []
print("Enter the non terminals :")
for _ in range(numberNonTerminals):
    nonTerminals.append(input())

startingSymbol = input("Enter the starting symbol: ")

noProductions = int(input("Enter no of productions: "))
productions = []
print("Enter the productions:")
for _ in range(noProductions):
    productions.append(input())

productionDict = {}
for nT in nonTerminals:
    productionDict[nT] = []

for production in productions:
    conversion = production.split("->")
    alternatives = conversion[1].split("/")
    for alternative in alternatives:
        productionDict[conversion[0]].append(alternative)

FIRST = {}

for non_terminal in nonTerminals:
    FIRST[non_terminal] = set()

for non_terminal in nonTerminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

print("{: ^20}{: ^20}".format('Non Terminals', 'First'))
for non_terminal in nonTerminals:
    print("{: ^20}{: ^20}".format(non_terminal, str(FIRST[non_terminal])))
