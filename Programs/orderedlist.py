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

    print("These are the data that we have in our File")

    file = open("/home/admin1/Documents/Shahazad/numbers.txt", "r")

    list = file.readlines()
    list = list[0]
    print(list)
    file.close()
  #  print("Enter data you are looking for")
    try:
        data = int(input("Enter the data to search"))
    except:
        print('Enter data in string only')
    print(orderedlist_obj.search_item(data))

    print("The updated file content are as follows")
    orderedlist_obj.file_update(data)


if __name__ == '__main__':
    orderedlist()

#     def __init__(self, data=None,next=None):
#         self.data = data
#         self.next = None
#         self.next_node = next
#
#     # def get_data(self):
#     #     return self.data
#     #
#     # def get_next(self):
#     #     return self.next
#     #
#     # def set_next(self, new_next):
#     #     self.next_node = new_next
#
#
# class LinkedList(object):
#     def __init__(self):
#         self.head = Node()
#
#     def insert(self, data):
#         new_node = Node(data)
#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = new_node
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current.next is not None:
#             count += 1
#             current = current.next
#         return count
#
#     def display(self):
#         elements = []
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#             elements.append(current_node.data)
#         print(elements)
#
#
#
# li = LinkedList()
#
# f = open("/home/admin1/Documents/Shahazad/numbers.txt", "r")
# words = []
# for line in f:
#     line = line.strip()
#     words += line.split(" ")
# li.insert(words)
# li.display()
# for i in range(len(words)):
#     s=words.sort()
#
# print(s)
#
#
#

