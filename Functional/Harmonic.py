from Utilities import utilities
def harmonic():
    try:
        n=int(input("Enter the nth Value"))
        utilities.Harmonic(n)
    except ValueError:
        print("Enter the Integer Number Only")



if __name__ == "__main__":
    harmonic()

