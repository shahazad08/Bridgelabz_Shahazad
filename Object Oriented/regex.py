"""
******************************************************************************
* Purpose:  Regular Expression, replacing the string
*
* @author:  Shahazad Shaikh
* @version: 3.7
*
******************************************************************************
"""
import re
import datetime
str1=' Hello <<name>>, We have your full name as <<full name>> in our system.\n your contact number is 91-xxxxxxxxxx.\n Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016. ' # String formation
try:
    first_name=input("Enter the First Name")
    full_name=input("Enter the Full Name")
    phone_no=input("Enter the Mobile Number with the standard format:955-804-1067")
    regex= "\w{3}-\w{3}-\w{4}"  # Given the format of the for the telephone number
    date=datetime.datetime.today().strftime('%d-%m-%Y') # format for a date
    if re.search(regex, phone_no): # takes a regular expression pattern and a string
        # and searches for that pattern within the string.
        print("Valid phone Number")
        str2 = re.sub("<<name>>", first_name, re.sub("<<full name>>", full_name, re.sub("xxxxxxxxxx", phone_no, re.sub("01/01/2016", date, str1)))) # Replacing the string pattern with the new string
        print(str2)

    else:
        print("Invalid Phone Number")

except ValueError:
        print("Name should be in a str")








