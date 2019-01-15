from Utilities.datastructure import Operations
def calender_stack():
    logic_obj = Operations()
    try:
        month = int(input("Enter the Month"))
        year = int(input("Enter the Year"))
    except:
        print("Enter integer only ")

    logic_obj.calender_queue(month, year)


if __name__ == "__main__":
    calender_stack()
