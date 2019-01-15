from Utilities import utilities
def coupon():
    try:
        coupon_no=int(input("Enter the Coupon Nos"))
        utilities.Coupon(coupon_no)

    except ValueError:
        print("Enter Number only")


if __name__ == "__main__":
   coupon()
