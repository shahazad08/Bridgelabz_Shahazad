from Utilities.datastructure import Deque

def palindrome_checker():
    deque=Deque()

    str1=input("Enter the String")
    lower_string = str1.lower()
    str1 = lower_string

    remove_space = ''
    # for i in range(0, len(str1)):
    #     if str1[i] == ' ':
    #         continue

       # remove_space += str1[i]

 #   str1 = remove_space

    for i in str1:
        deque.add_rear(i)
    reverse_string = ''
    for i in range(0, deque.size()):
        reverse_string += str(deque.remove_rear())

    if str1 == reverse_string:
        return True
    else:
        return False


if __name__ == "__main__":
    print(palindrome_checker())