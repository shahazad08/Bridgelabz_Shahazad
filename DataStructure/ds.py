class node:
    def __init__(self, data=None, next=None):
        self.data = data                         # data node
        self.next = None                         # last element of list will alwasys has none .
        self.next_node = next

    def get_data(self):                           # gets the data of node
        return self.data

    def get_next(self):                             # gets next node
        return self.next

    def set_next(self, new_next):                    # used while deleting: sets the next element to other next node.
        self.next = new_next


class linked_list:                                  # wrapper class for node class. user will never interface with node
    def __init__(self):
        self.head = node()                           # never gonna contain any actual data and not indexable.  simply used as placeholder to allow us to point to first node.

    def insert(self, data):                            # appends  element to list
        new_node = node(data)                           # creates a new node using class node .
        current = self.head                              # point to start iteration from ... first node
        while current.next != None:                          # while next element  is not Null
            current = current.next                              # sets the current node to next node
        current.next = new_node                             # create  the new node after current node

    def length(self):                                    # calculates length of list
        current = self.head                                 # at start nodes starts from Head
        total = 0                                           # variable to count the nodes.

        while current:                                      # while current = True
            total += 1                                        # incrementing total.
            current = current.get_next()                        # current element = next element until loop finishes
        return total

    def display(self):
        elemenst = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elemenst.append(current_node.data)
        print('data in linked list ', elemenst)
        findword = input("Enter the element to search ")
        my_list.search(findword, elemenst)


    def search(self, data, elemenst):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                print("Element found ")
            else:
                current = current.get_next()
        if current is None:
            print("Data was not in list and added to list")
            #my_list.add(data)
        return current

my_list = linked_list()
f = open("/home/admin1/Documents/Shahazad/myfile.txt", "r")
words = []
for line in f:
    words += line.split(" ")
#print(words)
my_list.insert(words)
my_list.display()
my_list