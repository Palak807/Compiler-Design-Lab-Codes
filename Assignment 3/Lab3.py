Grammar = str(input('Enter the Grammar : '))

if Grammar[0] == Grammar[5]:
    print('Left recursion exists')
    remove = Grammar.split('/')[1:]
    remove += Grammar[0] + '\''
    print(Grammar[0], '->', *remove)
    print(Grammar[0] + '\'', '->', Grammar.split('/')[0][6:], Grammar[0] + '\'','/', '∈')

else:
    print('Yayy!! Left recursion does not exist!!')