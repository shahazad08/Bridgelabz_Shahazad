from Utilities import utilities
try:
    m = int(input("Enter the Nth Elements"))
    print("Enter the elements")
    arr = [int(input()) for i in range(m)]
    print(arr)
    utilities.Bubble(arr)

    #raise NumericException
#except NumericException:
   # print("Only String Allowed")
except ValueError:
    print("Enter the Valid String")