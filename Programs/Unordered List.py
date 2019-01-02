from Utilities.datastructure import

# class Node(object):
#
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
#         key = input("Enter the element to search ")
#         li.search(key)
#
#
#     def search(self,data):
#         current = self.head
#         if self.head == None:  # execute if list empty
#             return False
#
#         while current.next != None:
#
#             if current.data == data:  # checks for matching data
#                 #return True
#                 print("Element Found")
#             current = current.next
#         if current.data == data:
#             print("Element Found")  # for single node
#         else:
#             print("Element Not Found")
#
# li = LinkedList()
# # li.display()
# # li.insert(1)
# # li.insert(2)
# # li.insert(3)
# # li.insert(4)
# # li.display()
# # a=(input("Enter key to search"))
# # print("Element at 2nd index:", li.search(a))
#
# f = open("/home/admin1/Documents/Shahazad/myfile.txt", "r")
# a=f.readlines()
# #words = []
# # for line in f:
# #     line = line.strip()
# #     words += line.split(" ")
# li.insert(a)
# li.display()
# #li.search(k)
# #key = (input("Enter the Key to search"))
#
#
# #print("bbhb",words)
# #
