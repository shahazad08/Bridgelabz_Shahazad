from Utilities import utilities
def uname():
    try:
        u_name=input("Enter the name")
        utilities.Uname(u_name)

    except ValueError:
        print("Enter Valid Input")


if __name__ == "__main__":
    uname()





