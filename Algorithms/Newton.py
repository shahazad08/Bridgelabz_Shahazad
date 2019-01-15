from Utilities import utilities
def newton():
    try:
        epsilon=1e-15
        no=int(input("Enter the Number"))
        t=no
        utilities.Newton(no,t,epsilon)

    except ValueError:
        print("Enter the Number Only")


if __name__ == '__main__':
    newton()



