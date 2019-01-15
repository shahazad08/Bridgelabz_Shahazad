def filesearch():
    try:
        f = open("myfile1.txt", "r")
        print(f.readlines())
        key = (input("Enter the word to be searched"))
        with open("myfile1.txt") as openfile:
            for line in openfile:
                for part in line.split():
                    if key in part:
                        print("Key is Found at line", part)
                    else:
                        print("Not Found")

    except FileNotFoundError:
        print("File Not Found")

if __name__ == '__main__':
   filesearch()

