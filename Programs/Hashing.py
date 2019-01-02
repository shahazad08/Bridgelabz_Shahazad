from Utilities.datastructure import HashTable
def hashing_runner():
    """
    This method acts as runner
    :return: nothing
    """
    hash_obj = HashTable()

    print('These are the Numbers in our File')
    file = open("/home/admin1/Documents/Shahazad/numbers.txt", "r")
    print(file.readline())

    #print('Now enter the Number you are looking for')
    try:
        number=int(input("Enter the Number u r looking for"))
    except:
        print("Enter Number only")
    hash_obj.insert()
    print(hash_obj.search(number))

    print('Now Updated File Content are as Follows')
    hash_obj.file_update(number)


if __name__ == "__main__":
    hashing_runner()