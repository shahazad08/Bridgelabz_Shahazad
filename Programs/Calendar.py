from Utilities.datastructure import calender_stack
from Utilities.datastructure import Logic

def calender_runner():
    """
    This method act as runner for calender_queue(month, year)
    :return: nothing
    """

    logic_obj = Logic()

    #print('Enter Month')
    try:
        month=int(input("Enter the Month"))
    except:
        print("Enter integer only ")
    try:
        year = int(input("Enter the Year"))
    except:
        print("Enter integer only")
    logic_obj.calender(month, year)


if __name__ == "__main__":
    calender_runner()