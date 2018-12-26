from Utilities import utilities
n=int(input("Enter the Number"))
ch=int(input("Enter the Choice"))
if(ch==1):
    utilities.BinaySearchInteger(n)
elif(ch==2):
    utilities.BinaySearchString(n)
elif(ch==3):
    utilities.InsertionSortInteger(n)
elif(ch==4):
    utilities.InsertionSortString(n)
elif(ch==5):
    utilities.BubbleSortInteger(n)
elif(ch==6):
    utilities.BubbleSortString(n)
else:
    print("Enter the Valid Choice")
