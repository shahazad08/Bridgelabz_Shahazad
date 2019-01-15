from Utilities import utilities
def insterion():
    try:
        m = int(input("Enter the Nth Elements"))
        print("Enter the elements")
        str1 = [(input()) for i in range(m)]
        print(str)
        utilities.Insertion(str1)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    insterion()
