from Utilities import utilities
keepGoing=1
while(keepGoing):
    m=int(input("Enter the Month"))
    if (m < 1 or m > 12):
        print("Months are between 1 and 12")


    d=int(input("Enter the Day"))
    if (d < 1 or d > 31):
        print("Days are between 1 and 31")


    y=int(input("Enter Year"))
    #print("Enter Year")
    if (y < -10000 or y > 10000):
        print("Years are between 10000 and 10000")


    utilities.DayofWeek(m,d,y)






