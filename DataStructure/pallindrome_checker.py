from Utilities.datastructure import Deque

def palindrome_checker():
    deque=Deque()

    try:
        str1=input("Enter the String")
        lower_string = str1.lower()
        str1 = lower_string

    except ValueError:
        print("Enter String Only")


    try:
        for i in str1:
            deque.add_rear(i)
        reverse_string = ''
        for i in range(0, deque.size()):
            reverse_string += str(deque.remove_rear())

        if str1 == reverse_string:
            return True
        else:
            return False

    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(palindrome_checker())