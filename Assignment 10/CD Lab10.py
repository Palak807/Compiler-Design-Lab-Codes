from tabulate import tabulate as tb


def Length(x, temp):
    originalLen = len(temp)
    if temp[0][:1] == "f":
        if originalLen % 2 != 0:
            return f"g({x})"
        else:
            return f"f({x})"
    elif temp[0][:1] == "g":
        if originalLen % 2 != 0:
            return f"f({x})"
        else:
            return f"g({x})"


def matrixValues(x, y):
    global variableList
    global matrix
    return matrix[variableList.index(x)][variableList.index(y)]


def inv(x):
    return -1 * x


def OPtable(variable):
    global variableList, entry
    x, y = 0, 0
    isRunning = True
    if variable[:1] == "f":
        check = 1
        nextValue = "b"
        if "id" in variable:
            value = variable[2:4]
        else:
            value = variable[2:3]
        entry, b = value, variableList[y]
    elif variable[:1] == "g":
        check = -1
        nextValue = "a"
        if "id" in variable:
            value = variable[2:4]
        else:
            value = variable[2:3]
        entry, b = variableList[x], value

    temp = [variable]

    while isRunning:
        if entry == "$" or b == "$":
            isRunning = False
        if matrixValues(entry, b) == check:
            if nextValue == "a":
                temp.append(Length(entry, temp))
                check = inv(check)
                nextValue = "b"
                y = 0
            else:
                temp.append(Length(b, temp))
                check = inv(check)
                nextValue = "a"
                x = 0
        elif entry == "$" or b == "$":
            if nextValue == "a":
                check = inv(check)
                nextValue = "b"
                y = 0
            else:
                check = inv(check)
                nextValue = "a"
                x = 0
        else:
            if nextValue == "a":
                x += 1
                entry = variableList[x]
            else:
                y += 1
                b = variableList[y]
    global result
    result.append(temp)


if __name__ == "__main__":
    productions = {}
    no_of_productions = int(input("Enter no of productions: "))

    grammar = []

    print("Enter the productions(Format : A-> abc/bc):")
    for _ in range(no_of_productions):
        grammar.append(input())

    print(grammar)

    variableCount = int(input("Enter the number of variables: "))
    variableList = []
    for i in range(variableCount):
        variableList.append(str(input(f'Enter the value of Variable-{i} : ')))

    result = []

    cells = int(input("Give the number of rows/columns in operator precedence table:"))

    matrix = []

    print("Enter the values of OP table row-wise separated by space (1 for >, -1 for <, 0 for =) ")
    for i in range(cells):
        row = list(map(int, input().split()))
        matrix.append(row)
    print("\nOperator Precedence Table\n")
    print(matrix)

    result = []

    func_list = []
    for _ in variableList:
        func_list.append(f"f({_})")
        func_list.append(f"g({_})")

    for _ in func_list:
        if _ != 0:
            OPtable(_)
            for j in result:
                for _ in j:
                    if _ in func_list:
                        func_list[func_list.index(_)] = 0

    functions = [" "]
    for i in variableList:
        functions.append(i)

    data = [functions]
    functions = ["f( )", 4, 4, 2, 0]
    data.append(functions)
    functions = ["g( )", 5, 3, 1, 0]
    data.append(functions)
    print("\nOperator Function Table\n")
    print(tb(data, tablefmt="grid"))

    print("\nFunction sequence from graph: \n")
    for i in result:
        for j in i:
            if j[2:-1] != "$":
                print(j, end=" -> ")
            else:
                print(j)
