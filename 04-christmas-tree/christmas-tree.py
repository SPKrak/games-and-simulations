# declare function
def printTree(fTreeHeight):

    # declare variables
    treeHeight = fTreeHeight
    line = 1
    columnCounter = 1
    asterix = "*"
    space = " "
    numOfSpaces = treeHeight - 1
    numOfAsterixes = 1

    # assign passed value
    treeHeight = fTreeHeight

    # header
    print("Chistmas Tree assignment")

    # declare row loop
    for line in range(treeHeight):

        # declare column loop for adding spaces
        for columnCounter in range(numOfSpaces):
            print(space, end="")

        columnCounter = 1

        # declare column loop for adding asterixes
        for columnCounter in range(numOfAsterixes):
            print(asterix, end="")

        # after everything is printed in the line, set amount of spaces and asterixes for the next line
        if numOfSpaces != 0:
            numOfSpaces -= 1
            numOfAsterixes += 2

        # and add the new line
        print()

# run program
userInput = int(input("Type in the height of the tree: "))
printTree(userInput)
