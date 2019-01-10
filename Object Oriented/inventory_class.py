"""
******************************************************************************
* Purpose:  Inventory Management System(Calculate Inventory)
*
* @author:  Shahazad Shaikh
* @version: 3.7
*
******************************************************************************
"""
import json

with open("../ObjectOrientedProgram/inventory.json", "r") as f:
    x = f.read()  # Reading the file
    f.close()
    inv = json.loads(x)  # Load the json file in inventory
print(inv)

cal_rice = 0  # intialize the counting of rice price to be 0
cal_wheat = 0
cal_pulses = 0
mycnt = 0

print("\n")
print("Details of Rice")
for rice in inv['Rice']:  # Each of a Rice elements are placed in a rice variable
    print(rice)
    cal_rice += int(rice['price per kg'])  # Calculate the price per kg and iterate each of the rice values
print(cal_rice)  # print the values of each rice price...

a = inv["Wheat"]  # Similar for a Wheat
print("\n")
print("Details of Wheat")
for wheat in a:
    print(wheat)
    mycnt = int(wheat['price per kg'])
    cal_wheat += mycnt
print(cal_wheat)

print("\n")

print("Details of Pulses")  # Similar for a Pulses
for pulse in inv['Pulses']:
    print(pulse)
    cal_pulses += int(pulse['price per kg'])
print(cal_pulses)
