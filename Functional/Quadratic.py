from Utilities import utilities
def quadratic():
    try:
        a = int(input("Enter the 1st No"))
        b = int(input("Enter the 2nd No"))
        c = int(input("Enter the 3rd No"))
        utilities.Quadratic(a, b, c)

    except ValueError:
        print("Enter Valid Input")

if __name__ == "__main__":
    quadratic()



