"""
******************************************************************************
* Purpose:  Commercial Data Processing
* @author:  Shahazad Shaikh
* @version: 3.7
*
******************************************************************************
"""
import json

class Person:
    try:
        def __init__(self):
            with open("stock.json", "r") as jf:
                stock_jf = json.load(jf)  # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def show_shares(self):
            for i in range(len(
                    self.stock_jf['Stock Report'])):  # Iterating through Stock Report by means of checking the length
                print(i, self.stock_jf['Stock Report'][i])

        def check_validity(self):

            print("*********** Welcome **************")
            i = 0
            name = input("Enter Username")
            while i < len(self.person_json_value["Person"]):  # Creating the user for buying or selling a shares
                if self.person_json_value["Person"][i]["Name"] == name.title():  # Verifying the user
                    index = i
                    print(self.person_json_value["Person"][i])
                    print("....Login successful....")
                    c = int(input("1:Buy shares\n2:Sell shares:"))
                    if c == 1:
                        p.buy_share(index)
                    elif c == 2:
                        p.sell_share(index)

                    else:
                        print("wrong Input")
                i += 1

        def add_new_company(self):  # Add a new company by adding a new through dictionary
            name = input("Enter company name")
            number = int(input("Enter Your Number of share"))
            price = int(input('Enter Your Price per share'))
            new_stock_dict = {"Stock Name": name,  # created the dictionary for a new values

                              "Number of Share": number,

                              "Share Price": price}

            with open('stock.json', 'w') as stock_jf:  # Add a new file in a json through a key
                self.stock_jf['Stock Report'].append(new_stock_dict)

                stock_jf.write(json.dumps(self.stock_jf, indent=2))  # Writing a file through python to json

        def buy_share(self, index):
            for i in range(len(self.stock_jf['Stock Report'])):    # Iterating through stock report for buying a shares
                print(i, self.stock_jf['Stock Report'][i])

            print('Enter Which Company Share you want to buy')
            choice = int(input("Enter choice in Int"))
            buy_share = int(input("Enter Number of Share You want to buy"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']  # Asking for a user to sell shares
            # among indexing
            amount_pay = buy_share * each_share_price   # Calculating the share that are purchasing

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay: # Balance shoud be
                # there while purchasing

                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay)
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share  # Updating the
                # stock
                with open("stock.json", "w") as jf:                    # Changing the updated stock in a file
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay   # Subtracting the new share
                # amount from a balance
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share    #Adding the new shares
                # in a stock
                print('Now Your Updated Number of share is ', person_updated_share)

                with open("customers.json", "w") as jf:  # Write to a file using a dump method
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:
                print("You Don't have enough money ")

        def sell_share(self, index):
            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

            choice = int(input("Enter choice in Int"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company') # Ask for a user which share u want to sell
            sell_share = int(input("Number of shares to sell "))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share  # New Share updates
            with open("stock.json", "w") as jf:
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share # Decrementing the shares

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share  # Changing acco

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)

            with open("customers.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))



    except Exception as e:
        print(e)


if __name__ == "__main__":
    p = Person()
    p.show_shares()
    try:
        i = int(input("1: Admin Login or 2: User "))
        if i == 1:                                      # If user selects Admin
            print("welcome Admin")
            j = int(input("1 to add Company :"))
            if j == 1:
                p.add_new_company()
        elif i == 2:                                    # if user selects User
            print("Welcome User")
            p.check_validity()

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid Value")
