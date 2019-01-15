from Utilities import utilities
def Euclidean():
    try:
        x = int(input("Enter the X Value"))
        y = int(input("Enter the Y Value"))
        utilities.Euclidean(x, y)
    except ValueError:
        print("Enter the Valid Input Number")


if __name__ == "__main__":
    Euclidean()