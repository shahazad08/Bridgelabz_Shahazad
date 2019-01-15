from Utilities import utilities
def binary():
    try:
        n=int(input("Enter the decimal Number"))
        str1=bin(n).replace("0b","")    # replace the ob(binary) to blank
        print("in binary.",str1)
        utilities.ToBinary(str1)
    except ValueError:
        print("Enter the Valid String")

if __name__ == '__main__':
    binary()


