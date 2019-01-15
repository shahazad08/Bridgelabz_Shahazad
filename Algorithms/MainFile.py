from Utilities import utilities
def file():
    try:
        f = open("myfile1.txt", "r")
        words = []
        key = input("Enter the Key to search")
        for line in f:
            words += line.split(" ")
            utilities.BinaySearchString(words,key)
        f.close()

    except FileNotFoundError:
        print("File Not Found")


if __name__ == '__main__':
    file()


