from Utilities import utilities
try:
    x = int(input("Enter the X Value"))
    y = int(input("Enter the Y Value"))
except ValueError:
    print("Enter the Valid Input Number")
except NameError:
    print("Enter the Valid Input")
    utilities.Euclidean(x, y)
