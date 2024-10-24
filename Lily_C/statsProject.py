import inspect
from typing import Callable, List
import math
from random import randint

menuDict = {}
def menu(key: str, argTypes: Callable): # The function called when you do @Menu()
    def decorator(fn: Callable): # The wrapper around the fn on the line below

        def wrapper(args):
            argsLen = len(args)
            typesLen = len(argTypes)

            if argsLen > typesLen:
                print(f'\x1b[0;33mToo many arguments provided, proceeding with first {typesLen}\x1b[0m')

            if argsLen < typesLen:
                print("\x1b[0;31mToo few arguments provided\x1b[0m")
                return None

            newArgs = []
            i = 0
            while i < argsLen and i < typesLen:
                try:
                    newArgs.append(argTypes[i](args[i]))
                except:
                    print(f'\x1b[0;31mArgument {i} must be of type {argTypes[i].__name__}\x1b[0m')
                    return None
                i += 1

            return fn(*newArgs)

        # convert function __name__ to a Title Case name for display
        name = bytearray(fn.__name__, "ascii")
        i = 0
        while i < len(name):
            if name[i] >= 65 and name[i] <= 90: # [A, Z]
                name.insert(i, 32) # 32 is Space
                i += 1 # increment extra to avoid retread
            i += 1
        name[0] -= 32 # makes first letter uppercase
        
        wrapper.__name__ = name.decode("ascii")

        menuDict[key] = (wrapper, fn) # store both the wrapped and original function

        # allows fn to still be looked up by name
        return fn

    return decorator


def showMenu():
    print("[#]=====[Function Name]===[Parameters]===") # add a little flair

    # display each menu item
    for key, (fn, ogFn) in menuDict.items():
        params = inspect.signature(ogFn).parameters
        # format the parameters
        paramStrs = []
        for k, v in params.items():
            paramStrs.append(str(k))
        paramsStr = str(paramStrs).replace("'", "")

        print(f'{key}:\t{fn.__name__}{" " * (18 - len(fn.__name__))}{paramsStr}')

    # display hardcoded Exit item
    print(
        "Exit:\tQuit the program\n"
        "----\n"
        "Example input: \x1b[0;36m2 arg1 arg2\x1b[0m\n"
        "> ",
        end=""
    )

def prompt(message: str):
    print(f'{message}:\n> ', end="")

# menu items

items: list[float] = []

@menu("1", [float])
def addValue(val):
    i = 0
    while(i < len(items) and val > items[i]):
        i += 1
    items.insert(i, val)

@menu("2", [float])
def removeValue(val):
    for i in range(len(items)):
        if items[i] == val:
            items.pop(i)
            return

@menu("3", [int])
def removeIndex(index):
    if 0 < index or index <= len(items): return
    items.pop(index)

@menu("4", [])
def displayList():
    # returning in a menu function will display that value
    return str(items) if items != [] else "Empty"

@menu("5", [])
def mean():
    if len(items) == 0: return
    
    total = 0
    for item in items:
        total += item
    return total/len(items)

@menu("6", [])
def median():
    length = len(items)
    if length == 0:
        return
    
    halfLen: int = length//2
    if length & 1 == 1:
        return items[halfLen]
    else:
        return (items[halfLen-1]+items[halfLen]) / 2

# returns the average of the first and last elements of the list
@menu("7a", [])
def midpoint():
    if len(items) == 0: return
    return (items[0] + items[-1]) / 2

# returns the middle index
@menu("7b", [])
def indexMidpoint():
    if len(items) == 0: return
    return items[len(items)//2]

@menu("8", [])
def mode():
    if len(items) == 0: return
    # value to amount of times it appears
    amounts = {}
    for item in items:
        amounts[item] = amounts.get(item, 0) + 1
    # the highest rankers
    best = 0
    bestList = []
    for k, v in amounts.items():
        if v == best:
            bestList.append(k)
        elif v > best:
            best = v
            bestList = [k]
    return bestList

@menu("9", [])
def standardDeviation():
    if len(items) == 0: return

    sum = 0
    # don't wanna call an O(n) opperation every loop when you don't have to
    listMean = mean()
    for item in items:
        sum += (item - listMean)**2

    return math.sqrt(sum/len(items))

alwaysShowList = False
@menu("Toggle", [])
def alwaysDisplay():
    global alwaysShowList
    alwaysShowList = not alwaysShowList

@menu("Fill", [int])
def populateList(elementCount):
    for _ in range(elementCount):
        items.append(randint(-100, 100))

    # I have to write sorting algorithms every week for CSCD 300
    # I get to call the builtin this one time
    items.sort()


# end setup
# start runtime

showMenu()
last = ""
while((inp := input()) != "Exit"):
    # clear leading/trailing whitespace
    inp = inp.strip() 
    # split over whitespace, creating an easy to use set of the input
    inp = inp.split()

    # the command is at index 0, popping so the rest of the set can be assumed at argument inputs
    inpItem = inp.pop(0)
    # allow up arrow to access the last command input
    if inpItem == "\x1b[A": # up arrow
        inpItem = last

    fn = menuDict.get(inpItem)

    if fn:
        # get specifically the wrapped function, [1] is the unwrapped
        fn = fn[0]

        out = fn(inp)
        # print the output with some flair
        if out != None:
            print(f'\x1b[0;32m{out}\x1b[0m')

        if alwaysShowList:
            print(f'\x1b[0;32m{items}\x1b[0m')
    else:
        print(f'\x1b[0;31m{inpItem} is not on the Menu\x1b[0m')

    last = inpItem
    showMenu()
