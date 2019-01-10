"""
******************************************************************************
* Purpose:  Maintaning and calculating Stock Report
*
* @author:  Shahazad Shaikh
* @version: 3.7
*
******************************************************************************
"""

import json
with open('../ObjectOriented/stock.json', 'r') as jf:
    json_str = jf.read()
    jf.close()
json_value = json.loads(json_str) # Read the file from json
print(json_value)

def stock_report(self):
    count = 0
    count1 = 1

    for i in range(len(json_value['Stock Report'])): # Place the value of a stock report in i
        count1 = 1
        for key in (json_value['Stock Report'][i]): # use i as an index to place the key value

            if i == 0 and count == 0:               # if its zero
                for key1 in (json_value['Stock Report'][0]):    # place the stock report of 0th index to key1
                    print(key1, end=' ')                        # print key
                    count += 1                                  # add cnt by 1
                    if count == len(json_value['Stock Report'][0]): # print each of the total
                        # price from the key index of a stock report
                        print(' Total Price ', end=' ')

                print()

            print(json_value['Stock Report'][i][key], end='\t\t\t') # Place the value of a stock report in i
            if count1 == len(json_value['Stock Report'][i]):    # Iterate through the indexing of a stock report
                print(json_value['Stock Report'][i]['Number of Share'] * json_value['Stock Report'][i]['Share Price'],
                    end='\t\t') # calculate the price of a stocks
            count1 += 1 # iterate cnts to 1+
        print()

stock_report(self=None)