from Utilities import utilities
def watch():
    try:
        a=int(input("Press [0-9] key to start the time"))
        b=int(input("Press [0-9] key to Stop the time"))
        utilities.Start1()
        utilities.Stop1()
        utilities.Elapsedtime()

    except ValueError:
        print("Invalid Input")

if __name__ == "__main__":
    watch()




