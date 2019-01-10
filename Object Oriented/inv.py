"""
******************************************************************************
* Purpose:  Inventory Management System(Adding New Records)
*
* @author:  Shahazad Shaikh
* @version: 3.7
*
******************************************************************************
"""
import json

with open("../ObjectOrientedProgram/inventory.json", "r") as f:
    s = f.read()
    f.close()
    inv = json.loads(s)   #json.loads(load string) is used when loading a string.

print(inv)
print(type(inv))          # shows in a dictionary format



print("Enter the Names to be add in")
print("1. Rice ")
print("2. Wheat ")
print("3. Pulses ")
ch=int(input())                             # Entering as per the user
if ch == 1:
    newrice_name = input("Enter the new rice")
    newrice_weight = input("Enter the weight")
    newricer_price = input("Enter the price per kg")
    with open("../ObjectOrientedProgram/inventory.json","w") as f:
        inv["Rice"].append({"name":  newrice_name , "weight":  newrice_weight, "price per kg":newricer_price})  # Append the new data to the file
        f.write(json.dumps(inv, indent=2))      #write the new values to the json file using dumps method
        f.close()

    with open("../ObjectOrientedProgram/inventory.json", "r") as f:  # Loads the file
        s = f.read()
        inv = json.loads(s)         # Read the new file
        print(inv)

elif ch==2:
    newheat_name = input("Enter the new Wheat")         # Similar same for a Wheat
    newheat_weight = input("Enter the weight")
    newheat_price = input("Enter the price per kg")
    with open("../ObjectOrientedProgram/inventory.json","w") as f:
        inv["Wheat"].append({"name": newheat_name, "weight":  newheat_weight, "price per kg":  newheat_price})
        f.write(json.dumps(inv, indent=2))
        f.close()

    with open("../ObjectOrientedProgram/inventory.json", "r") as f:
        s = f.read()
        inv = json.loads(s)
        print(inv)


elif ch==3:                                              # Similar same for a Wheat
    newpulse_name = input("Enter the new Pulses")
    newpulse_weight = input("Enter the weight")
    newpulse_price = input("Enter the price per kg")
    with open("../ObjectOrientedProgram/inventory.json","w") as f:
        inv["Pulses"].append({"name": newpulse_name, "weight":  newpulse_weight , "price per kg": newpulse_price})
        f.write(json.dumps(inv, indent=2))   # dump JSON into a file. json.dumps(dump string) is used when we need
        # the JSON data as a string for parsing or printing.
        f.close()

    with open("../ObjectOrientedProgram/inventory.json", "r") as f:
        s = f.read()
        inv = json.loads(s)
        print(inv)














