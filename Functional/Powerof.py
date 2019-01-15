from Utilities import utilities
def power():
    try:
        n=int(input("Enter the Nth Value"))
        utilities.Power(n)
    except ValueError:
        print("Enter Number only")

if __name__ == "__main__":
    power()

