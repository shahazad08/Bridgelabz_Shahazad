from Utilities import utilities
def twodarray():
    try:
        m=int(input("Enter the No. of rows"))
        n=int(input("Enter the No. of Columns"))
        utilities.Twoarray(m, n)

    except ValueError:
        print("Enter valid Input")

#print(matrix)


""""
for i in range(m):
    for j in range(n):
        a=int(input("Enter the Array of Elements"))
    print(a)
"""
"""
arr2= [int(input()) for i in range(m)]
arr3= [int(input()) for j in range(n)]
l=[arr2,arr3]
print(l)"""

