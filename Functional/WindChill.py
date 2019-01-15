from Utilities import utilities
def tf():
    try:
        temp=int(input("Enter the Tempreature (Fahrenheit)"))
        windSpeed=int(input("Enter the Wind Speed"))
        utilities.Wind(temp,windSpeed)

    except ValueError:
        print("Enter Valid input")

if __name__ == "__main__":
    tf()

