import json
from Utilities.datastructure import *

ll = LinkedList()
with open("stock.json", "r") as jf:  # converting a
    stock = json.load(jf)

for i in stock['Stock Report']:
    ll.append(i)
print(ll.display_content())
print(ll.size())

name = input(" Enter the name of Share")
number = int(input("Enter no of Shares"))
price = int(input("Enter the price"))

add = {
      "Stock Name": name,
      "Number of Share": number,
      "Share Price": price
}

ll.append(add)
print(ll.size())
print(ll.display_content())

add_stock = {"Stock Report": []}
for item in ll.display_content():
    add_stock["Stock Report"].append(item)


with open("stock.json", "w") as f:
    data = json.dumps(add_stock, indent=2)
    f.write(data)
print(data)

print("Enter the Company to be delete")
with open('stock.json', 'r') as jf:
    data = json.load(jf)
for element in int(data):
    if'abcd' in element:
        del element['abcd']
        print("")

with open('stock.json', 'w') as jf:
    data = json.dump(data,jf)





























# from Utilities.datastructure import *
# import json
# class Person:
#     try:
#         def __init__(self):
#             with open("stock.json", "r") as jf:
#                 stock_jf = json.load(jf)  # load() convert file into python from json
#             print(stock_jf)
#
#             self.stock_jf = stock_jf
#             with open("customer.json", "r") as person_json_value:
#                 person_json_value = json.load(person_json_value)
#             self.person_json_value=person_json_value
#             print(person_json_value)
#
#         def addrecord(self):
#             name = input("Enter company name")
#             number = int(input("Enter Your Number of share"))
#             price = int(input('Enter Your Price per share'))
#             new_stock_dict = {"Stock Name": name,
#
#                               "Number of Share": number,
#
#                               "Share Price": price}
#             obj1 = LinkedList()
#             print(obj1.append(self.stock_jf))
#
#     except Exception as e:
#         print(e)
#
