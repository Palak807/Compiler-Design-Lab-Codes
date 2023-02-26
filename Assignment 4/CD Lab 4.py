def input_grammar():
    gram = {}
    total_var_num = int(input("Enter the Total Number of Variables: "))
    print("Enter All Variables")
    for i in range(total_var_num):
        all_var.append(input())

    for i in all_var:
        temp_prod = []
        print("Enter the production of Variable {} separated by '/'".format(i))
        temp_prod.append(input())
        gram[i] = temp_prod
    return gram


def removeDirectLR(gramA, A):
    """gramA is dictonary"""
    temp = gramA[A]
    tempCr = []
    tempInCr = []
    for i in temp:
        if i[0] == A:
            # tempInCr.append(i[1:])
            tempInCr.append(i[1:] + [A + "'"])
        else:
            # tempCr.append(i)
            tempCr.append(i + [A + "'"])
    tempInCr.append(["e"])
    gramA[A] = tempCr
    gramA[A + "'"] = tempInCr
    return gramA


def checkForIndirect(gramA, a, ai):
    if ai not in gramA:
        return False
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] == ai:
            return False
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
    return False


def rep(gramA, A):
    temp = gramA[A]
    newTemp = []
    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            t = []
            for k in gramA[i[0]]:
                t = []
                t += k
                t += i[1:]
                newTemp.append(t)

        else:
            newTemp.append(i)
    gramA[A] = newTemp
    return gramA


def rem(gram):
    c = 1
    conv = {}
    gramA = {}
    revconv = {}
    for j in gram:
        conv[j] = "A" + str(c)
        gramA["A" + str(c)] = []
        c += 1

    for i in gram:
        for j in gram[i]:
            temp = []
            for k in j:
                if k in conv:
                    temp.append(conv[k])
                else:
                    temp.append(k)
            gramA[conv[i]].append(temp)

    # print(gramA)
    for i in range(c - 1, 0, -1):
        ai = "A" + str(i)
        for j in range(0, i):
            aj = gramA[ai][0][0]
            if ai != aj:
                if aj in gramA and checkForIndirect(gramA, ai, aj):
                    gramA = rep(gramA, ai)

    for i in range(1, c):
        ai = "A" + str(i)
        for j in gramA[ai]:
            if ai == j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    op = {}
    for i in gramA:
        a = str(i)
        for j in conv:
            a = a.replace(conv[j], j)
        revconv[i] = a

    for i in gramA:
        l = []
        for j in gramA[i]:
            k = []
            for m in j:
                if m in revconv:
                    k.append(m.replace(m, revconv[m]))
                else:
                    k.append(m)
            l.append(k)
        op[revconv[i]] = l

    return op


def first(gram, term):
    a = []
    if term not in gram:
        return [term]
    for i in gram[term]:
        if i[0] not in gram:
            a.append(i[0])
        elif i[0] in gram:
            a += first(gram, i[0])
    return a


if __name__ == '__main__':
    firsts = {}
    separated_prods = []
    all_var = []
    prod = []
    gram = input_grammar()
    print(gram)
    result = rem(gram)
    for i in result:
        firsts[i] = first(result, i)
        print(f'First({i}):', firsts[i])
