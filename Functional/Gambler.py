from Utilities import utilities
def gambler():
    try:
        stakes=int(input("Enter the Stakes"))
        goals=int(input("Enter the Goals"))
        trials=int(input("Enter the Trials"))
        utilities.Gambler(stakes, goals, trials)

    except ValueError:
        print("Enter the Numbers only")


if __name__ == "__main__":
    gambler()
