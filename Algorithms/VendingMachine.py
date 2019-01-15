from Utilities import utilities
def vending():
    try:
        money=int(input("Enter the change in Rs to be returned by the Vending Machine"))
        utilities.VendingMachine(money)

    except ValueError:
        print("Enter the Rs. in Numbers only")

if __name__ == '__main__':
   vending()


