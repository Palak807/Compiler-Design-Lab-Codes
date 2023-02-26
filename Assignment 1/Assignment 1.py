filename = "test.txt"
numberOfLines = 0
with open(filename, 'r') as file:
    num = len(file.readlines())
    print("Total number of lines are: {}".format(num))

numberOfComments = 0
lineCount = 0
file = open('test.txt')
content = file.readlines()
for text in content:
    lineCount += 1
    if text.startswith("//") or text.startswith("#"):
        numberOfComments += 1
        print("There is a comment on line number: {}".format(lineCount))
    elif text.startswith("/*"):
        numberOfComments += 1
        print("There is a multiline comment started at line number: {}".format(lineCount))
    elif text.endswith("*/\n"):
        print("The multiline comment ended at line number: {}".format(lineCount))

print("Total number of comments are: {} ".format(numberOfComments))
