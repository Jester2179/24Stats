def printRectangle(height, width):
    area = height * width
    perimeter = 2 * (height + width)
    print(f"A rectangle with the height of: {height} and a width of: {width} has an area of: {area} and a perimeter of: {perimeter}")

def uiRectangle():
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    printRectangle(height, width)

def menuItemOne():
    printRectangle(3.55, 2.54)

def menuItemTwo():
    uiRectangle()

def menuItemThree():
    hole = int(input("Enter hole number: "))
    par = int(input("Enter par value: "))
    strokes = int(input("Enter number of strokes: "))

    # Check actual stroke numbers first
    if strokes == 1:
        result = "Hole in One!"
    elif strokes == 4:
        result = "Sailboat"
    elif strokes == 8:
        result = "Snowman"
    elif strokes == 10:
        result = "Bo Derek"
    elif strokes == par * 2:
        result = "Beagle"
    else:
        # Calculate difference from par
        diff = strokes - par
        if diff == -5:
            result = "Ostrich"
        elif diff == -4:
            result = "Condor"
        elif diff == -3:
            result = "Albatross"
        elif diff == -2:
            result = "Eagle"
        elif diff == -1:
            result = "Birdie"
        elif diff == 0:
            result = "Even Par"
        elif diff == 1:
            result = "Bogey"
        elif diff == 2:
            result = "Double Bogey"
        elif diff == 3:
            result = "Triple Bogey"
        else:
            result = f"{diff} over par"

    print(f"Hole {hole}: {result}")

def menuItemFour():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    total = sum(x for x in range(start, end + 1) if x not in [3, 4, 5])
    print(f"Total: {total}")

def menuItemFive():
    import random
    rolls = int(input("Enter number of rolls: "))
    counts = {i: 0 for i in range(2, 13)}
    doubles = 0

    for _ in range(rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1
        if die1 == die2:
            doubles += 1

    for total in range(2, 13):
        percentage = (counts[total] / rolls) * 100
        print(f"Sum {total}: {counts[total]} rolls ({percentage:.2f}%)")
    print(f"Doubles: {doubles} rolls ({(doubles/rolls)*100:.2f}%)")

def menuItemSix():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    palindromes = [num for num in range(start, end + 1)
                  if str(num) == str(num)[::-1]]
    total = sum(palindromes)
    print(f"Sum of palindromic numbers: {total}")

def menuItemSeven():
    print("Exiting program...")
    exit()

def menu():
    user = 0
    while user != 7:
        printMenu()
        user = int(input("type in the number of your choice"))
        if user == 1:
            menuItemOne()
        if user == 2:
            menuItemTwo()
        if user == 3:
            menuItemThree()
        if user == 4:
            menuItemFour()
        if user == 5:
            menuItemFive()
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()

def printMenu():
    print("1. rectangle")
    print("2. rectangle 2")
    print("3. golf")
    print("4. exclusive list")
    print("5. dice")
    print("6. palindrome")
    print("7. exit")
def menuItemOne():
    print("This is Menu Item 1")
def menuItemTwo():
    print("This is Menu Item 2")
def menuItemThree():
    print("This is Menu Item 3")
def menuItemFour():
    print("This is Menu Item 4")
def menuItemFive():
    print("This is Menu Item 5")
def menuItemSix():
    print("This is Menu Item 6")
def menuItemSeven():
    print("This is Menu Item 7")
