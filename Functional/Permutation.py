from Utilities import utilities
def permutation():
    try:
        s1=input("Enter the String")
        for p in utilities.permutation(s1):
            print(p)

    except ValueError:
        print("Enter the valid string")


if __name__ == "__main__":
    permutation()


