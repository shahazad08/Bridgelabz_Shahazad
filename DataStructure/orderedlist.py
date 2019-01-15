from Utilities.datastructure import OrderedList
def orderedlist():
    orderedlist_obj = OrderedList()

    file = open("/home/admin1/Documents/Shahazad/numbers.txt", "r+")

    list = file.readlines()
    file_string = list[0]

    list = file_string.split()

    for i in range(0, len(list)):
        orderedlist_obj.add(list[i].strip())
    file.close()
    print(list)
    try:
        data = int(input("Enter the data to search"))
    except:
        print('Enter data in string only')
    print(orderedlist_obj.search_item(data))

    print("The updated file content are as follows")
    orderedlist_obj.file_update(data)


if __name__ == '__main__':
    orderedlist()

