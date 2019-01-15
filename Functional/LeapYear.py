from Utilities import utilities
def leap():
    try:
        year = int(input("Enter the Year"))
        utilities.Leap(year)
    except ValueError:
        print("Enter the Year in Numbers Only")


if __name__ == "__main__":
    leap()




