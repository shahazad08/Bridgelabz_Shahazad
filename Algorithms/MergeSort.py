from Utilities import utilities

try:
    m = int(input("Enter the Nth Elements"))
    print("Enter the elements")
    str1 = [(input()) for i in range(m)]
   # print(str)

    utilities.MergeSort(str1)
except Exception as e:
    print(e)
except RecursionError:
    print("")