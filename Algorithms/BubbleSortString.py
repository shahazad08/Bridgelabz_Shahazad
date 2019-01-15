from Utilities import utilities
def bubble():
    try:
        m = int(input("Enter the Nth Elements"))
        print("Enter the elements")
        arr = [int(input()) for i in range(m)]
        print(arr)
        utilities.Bubble(arr)
    except ValueError:
        print("Enter the Valid String")

if __name__ == '__main__':
    bubble()