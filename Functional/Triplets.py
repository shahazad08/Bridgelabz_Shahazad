from Utilities import utilities
def triplets():
    try:
        m=int(input("Enter the No. of rows"))
        print("Enter the array elements")
        arr= [int(input()) for i in range(m)]
        print(arr)
        utilities.Triplets(arr)

    except ValueError:
        print("Enter valid input")

if __name__ == "__main__":
    triplets()


