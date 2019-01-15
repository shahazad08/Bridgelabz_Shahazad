from Utilities import utilities
def temp():
    try:
        fahrenheit =int(input("Enter the Tempreature in Fahrenheit:"))
        celsius=int(input("Enter the Tempreature in Celsius"))
        utilities.temperaturConversion(fahrenheit,celsius)

    except ValueError:
        print("Enter Number Only")

if __name__ == '__main__':
    temp()


