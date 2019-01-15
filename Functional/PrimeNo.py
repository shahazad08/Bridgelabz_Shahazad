from Utilities import utilities
def prime():
    try:
        n = int(input("Enter the nth value"))
        utilities.Prime(n)
    except ValueError:
        print("Enter Valid input")

if __name__ == "__main__":
    prime()
