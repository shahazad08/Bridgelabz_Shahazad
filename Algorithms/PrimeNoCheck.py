from Utilities import utilities
def prime():
    try:
        no1=int(input("Enter the First Number"))
        no2=int(input("Enter the Second Number"))
        utilities.PrimeCheck(no1,no2)

    except ValueError:
        print("Enter Number Only")


if __name__ == '__main__':
    prime()

