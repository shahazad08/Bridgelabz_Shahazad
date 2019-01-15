from Utilities import utilities
def sortingsearies():
    n = int(input("Enter the Number"))
    ch = int(input("Enter the Choice"))
    if ch == 1:
        utilities.BinaySearchInteger(n)
    elif ch == 2:
        print("Enter the String Elements")
        arr = [(input()) for i in range(5)]
        key = input("Enter the Key to search")
        l = []
        l = list(arr)
        utilities.BinaySearchString(l, key)
    elif ch == 3:
        utilities.InsertionSortInteger(n)
    elif ch == 4:
        utilities.InsertionSortString(n)
    elif ch == 5:
        utilities.BubbleSortInteger(n)
    elif ch == 6:
        utilities.BubbleSortString(n)
    else:
        print("Enter the Valid Choice")

if __name__ == '__main__':
    sortingsearies()

