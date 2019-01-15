from Utilities import utilities
def anagram():
    try:
        str1 = input("Enter the 1st String")
        str2 = input("Enter the 2nd String")
        utilities.Anagrams(str1,str2)
    except ValueError:
        print("Enter the Valid String")


if __name__ == '__main__':
    anagram()


