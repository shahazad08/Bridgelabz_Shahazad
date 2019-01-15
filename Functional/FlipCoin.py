from Utilities import utilities
def flips():
    try:
        n=int(input("Enter the Number of time to flip the coin"))
        utilities.Flips(n)

    except ValueError:
        print("Enter the Valid Input")


if __name__ == "__main__":
    flips()

