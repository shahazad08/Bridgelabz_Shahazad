from Utilities import utilities
import math
def questions():
    try:
        k = int(input("How many Steps you want to find your No"))
        n=math.pow(2,k)
        print("Think of Integer between %d to %d:", 0,"to",n-1)
        secret=utilities.Search(0,n)
        print("Your Number is",secret)
    except Exception as e:
        print("Enter the Integer Number Only")


if __name__ == '__main__':
    questions()







