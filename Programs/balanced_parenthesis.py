from Utilities.datastructure import Stack
def balance_parentheses():
    stack1 = Stack()
    try:
        str1=input("Enter Expression to check for balanced Parentheses")
    except Exception as e:
        print(e)
        print("Enter String")

    stack1.balanced_parentheses(str1)


if __name__ == "__main__":
    balance_parentheses()
