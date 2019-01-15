from Utilities import utilities
def dayofweek():
    try:
        run = 1
        while run:
            m = int(input("Enter the Month"))
            if m < 1 or m > 12:
                print("Months are between 1 and 12")

            d = int(input("Enter the Day"))
            if d < 1 or d > 31:
                print("Days are between 1 and 31")

            y = int(input("Enter Year"))
            if y < -10000 or y > 10000:
                print("Years are between 10000 and 10000")
            utilities.DayofWeek(m, d, y)
    except ValueError:
        print("Enter the Valid String")

if __name__ == '__main__':
    dayofweek()
