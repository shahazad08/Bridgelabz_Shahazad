


#pallindrome(n)


def pallindrome():
    n = int(input("Entee rthe Nos"))
    n1=str(n)
    a=n1[::-1]
    if(a==n1):
        print("Given Nos. is Pallindrome",a)
    else:
        print("Not the Pallindrome Nos")
    return 0

pallindrome()