import re

import pandas as pd
from tabulate import tabulate


def First(s, productions):
    first = set()
    for i in range(len(productions[s])):

        for j in range(len(productions[s][i])):

            c = productions[s][i][j]

            if c.isupper():
                f = First(c, productions)
                if 'ε' not in f:
                    for k in f:
                        first.add(k)
                    break
                else:
                    if j == len(productions[s][i]) - 1:
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('ε')
                        for k in f:
                            first.add(k)
            else:
                first.add(c)
                break

    return first


def Follow(start, productions, firstVal):
    followVal = set()
    if len(start) != 1:
        return {}
    if start == list(productions.keys())[0]:
        followVal.add('$')

    for i in productions:
        for j in range(len(productions[i])):
            if start in productions[i][j]:
                idx = productions[i][j].index(start)

                if idx == len(productions[i][j]) - 1:
                    if productions[i][j][idx] == i:
                        break
                    else:
                        f = Follow(i, productions, firstVal)
                        for x in f:
                            followVal.add(x)
                else:
                    while idx != len(productions[i][j]) - 1:
                        idx += 1
                        if not productions[i][j][idx].isupper():
                            followVal.add(productions[i][j][idx])
                            break
                        else:
                            f = First(productions[i][j][idx], productions)

                            if 'ε' not in f:
                                for x in f:
                                    followVal.add(x)
                                break
                            elif 'ε' in f and idx != len(productions[i][j]) - 1:
                                f.remove('ε')
                                for k in f:
                                    followVal.add(k)

                            elif 'ε' in f and idx == len(productions[i][j]) - 1:
                                f.remove('ε')
                                for k in f:
                                    followVal.add(k)

                                f = Follow(i, productions, firstVal)
                                for x in f:
                                    followVal.add(x)

    return followVal


def parsingTable(productions, first, follow):
    print("\nParsing Table (^◡^ )\n")

    OGtable = {}
    for key in productions:
        for value in productions[key]:
            val = ''.join(value)
            if val != 'ε':
                for element in first[key]:
                    if element != 'ε':
                        if not val[0].isupper():
                            if element in val:
                                OGtable[key, element] = val
                            else:
                                pass
                        else:
                            OGtable[key, element] = val
            else:
                for element in follow[key]:
                    OGtable[key, element] = val

    newTable = {}
    for pair in OGtable:
        newTable[pair[1]] = {}

    for pair in OGtable:
        newTable[pair[1]][pair[0]] = OGtable[pair]

    df = pd.DataFrame(newTable)
    df.fillna('---', inplace=True)
    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == "__main__":
    productions = {}
    no_of_productions = int(input("Enter no of productions: "))

    grammar = []

    print("Enter the productions(Format : A-> abc/bc):")
    for _ in range(no_of_productions):
        grammar.append(input())

    first = {}
    follow = {}
    table = {}

    start = ""

    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)
        m = []
        for i in l:
            if i == "" or i is None or i == '\n' or i == " " or i == "-" or i == ">":
                pass
            else:
                m.append(i)

        left_prod = m.pop(0)
        right_prod = []
        t = []

        for j in m:
            if j != '/':
                t.append(j)
            else:
                right_prod.append(t)
                t = []

        right_prod.append(t)
        productions[left_prod] = right_prod

        if start == "":
            start = left_prod

    for s in productions.keys():
        first[s] = First(s, productions)

    for lhs in productions:
        follow[lhs] = set()

    for s in productions.keys():
        follow[s] = Follow(s, productions, first)

    parsingTable(productions, first, follow)
