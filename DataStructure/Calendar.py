from Utilities.datastructure import calender_stack
from Utilities.datastructure import Operations

def calender():
    """
    This method act as runner for calender_queue(month, year)
    :return: nothing
    """

    logic_obj = Operations()

    #print('Enter Month')
    try:
        month=int(input("Enter the Month"))
        year = int(input("Enter the Year"))
    except:
        print("Enter integer only ")

    logic_obj.calender(month, year)


if __name__ == "__main__":
    calender()