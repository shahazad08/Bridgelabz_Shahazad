from Utilities.datastructure import Queue

def cash_counter():
    queue =Queue()
    bank_cash = 1000
    try:
        no_of_people =int(input("Enter the no of people in integer only"))
    except Exception as e:
        print(e)
    for i in range(0, no_of_people):
        queue.enqueue(i)

    print('Welcome To Bridgelabz Bank')
    for i in range(0, queue.size()):
        print('1.Deposit cash \n 2.Withdraw cash')
        choice =int(input())

        if choice == 1:
            print("Enter Deposit Amount ")
            try:
                deposit_amount = int(input())
            except Exception as e:
                print(e)
                print("Enter amount in integer only")
            bank_cash = bank_cash + deposit_amount
            #queue.dequeue()

        if choice == 2:
            print("Enter How much cash you want to Withdraw")
            try:
                withdraw_amount = int(input())
            except Exception as e:
                print(e)
                print("Enter withdraw amount in integer only")
            if withdraw_amount < bank_cash:
                bank_cash = bank_cash - withdraw_amount
                queue.dequeue()

            if withdraw_amount > bank_cash:
                print('Insufficient Fund in Bank')
                print('1. Kindly enter cash within ' + str(bank_cash) + ' range  \n 2.If you do not want and leave')
                withdraw_choice = int(input())

                if withdraw_choice == 1:
                    print('Enter Withdraw Amount')
                    try:
                        withdraw_amount = int(input())
                    except:
                        print("Enter withdraw amount in integer only")
                    if withdraw_amount <= bank_cash:
                        bank_cash = bank_cash - withdraw_amount
                    queue.dequeue()

                if withdraw_choice == 2:
                    queue.dequeue()

        if i < queue.size():
            print('Next Person')

    print('Bank Balance => ' + str(bank_cash))


if __name__ == "__main__":
    cash_counter()