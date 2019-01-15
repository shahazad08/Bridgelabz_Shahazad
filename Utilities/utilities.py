import random
import math
import time
import numpy as np
import collections


# ****************************** 1.User Inputs************************************#
#  Purpose: Replace String Template
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   21-12-2018
# */


def Uname(u_name):
    if len(u_name) > 3:  # Check the Username Should me minimum 3 char
        print("The ActualName is", u_name)
        new_name = input("Enter the name to be change")
        if len(new_name):  # if True, Replace the old name with the new name
            print("Hello", new_name, "How r u?")
        else:
            print("Enter the Valid Name")
    else:
        print("Wrong Input")


# ****************************** 2. Flip Coins  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   21-12-2018
# */

def Flips(n):
    head = 0
    tails = 0
    for i in range(0, n):  # Checking the Random Number between 0 to N
        coins = random.randint(0, 1)  # Generates Random Number till N
        if (coins < 0.5):  # if Coins less than 0.5
            tails = tails + 1
        else:
            head = head + 1
    print("Total No. of Heads", head)
    print("Total No. of Heads", tails)
    print("Total No. of Head Generated", head / n)
    print("Total No. of Tails Generated", tails / n)


# ****************************** 3. Leap Year************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author Shahazad Shhaikh
#  *  @version 3.7
#  *  @since   21-12-2018
# */
def Leap(year):
    if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):  # Condition to check a Leap year
        print("The Given Year is a Leap Year")
    else:
        print("The Given Year is Not the Leap Year")


# ****************************** 4. Power of 2 ************************************#
#  Purpose: Determines prints a table of the powers of 2 that are less than or equal to 2^N.
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 1.0
#  *  @since   21-12-2018
#
# */

def Power(n):
    mul = 2
    if n < 31:  # Power of a 2 shouls be less than 31, if it is greater than overflow
        for i in range(1, n + 1):  # Iterating the Lopp from 1 to N+1 for calculating the power of 2
            print("Power of the 2 is", 2 ** i)  # Printing 2*i,2*i+1....
    else:
        print("Overflows the Integer")


# ****************************** 5. Harmonic Number ************************************#
#  Purpose: Series of a Harmonic Number
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   21-12-2018
#
# */

def Harmonic(n):
    h = 0   # Intialize Harmonic Value to 0
    for i in range(1, n):  # Iterating the loop till nth value
        h = 1 / i  # Dividing each element for generaring the series 1/1 + 1/2 + 1/3 + ... + 1/N
    print(h)


# ****************************** 6. Prime Nos Factorization ************************************#
#  Purpose: Computes the prime factorization of N
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   21-12-2018
#
# */

def Prime(n):
    fact = 2
    for fact in range(fact, n):  # Iterating the Loop From Fact to N
        while n % fact == 0:  # Checking when number is divisible by fact
            print(" Factor is", fact)  # Print Fact
            n = n / fact  # Reducing Number


# ****************************** 7. Gambler Program ************************************#
#  Purpose: Gambler Program
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   21-12-2018
#
# */
def Gambler(stakes, goals, trials):
    bets = wins = i = 0
    for i in range(i, trials):  # Iterating through 0 till game play
        cash = stakes
        while 0 < cash < goals:  # Iterate till Cash greater than 0 and cash less than goals
            bets += 1
            a = random.uniform(0, 1)  # Generate Random Number
            if a < 0.5:  # If Number greater than 0.5 than cash will increase
                cash += 1
            else:
                cash = cash - 1  # Else Cash Decrease
        if cash == goals:  # Cash is Equal to goals then Win
            wins += 1
    print(wins, "Wins of", trials)
    print("Percentage of Game Wins", 100.0 * wins / trials)
    print("Average of Bets", 1.0 * bets / trials)


# ****************************** 8. Coupon Numbers ************************************# Purpose: Generation of a
# Coupon Numbers with n distinct coupon number i.e how many random no. thay have generate to get the discinct coupon
# nos.
# * *  @author Shahazad Shaikh
# *  @version 3.7 *
# @since   22-12-2018
#
# */

def Coupon(coupon_no):
    l = []  # Empty List
    count = 0
    l = [int(i) for i in str(coupon_no)]  # Generating the Coupon Number in a list one by one
    print(l)
    while len(l) > 0:  # Iterate length of list should be greater than 0
        number = random.randint(0, 9)  # Generates the random number[0-9]
        count += 1
        if (
                number in l):  # If random no. is found in the list, then remove the no. generate the count till how
                                    # many random no. thay have generate to get the discinct coupon nos.
            l.remove(number)
            print(l)

    print("Total random numbers to generate coupoun", count)


# ****************************** 9. 2D Array  ************************************#
#  Purpose: Reading the 2D Array and Print it...
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   22-12-2018
#
# */

def Twoarray(m, n):  # Call the m as a row and n as a columns
    matrix = [[0 for j in range(m)] for i in
              range(n)]  # Print the matrix 2X2 or 3X3 with [0,0,0] as per the range i,e creating the space the 0's
    print(matrix)

    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(input("Enter the Array Elements"))  # Enters the element in a row and columns in a list

    array = np.array(matrix)  # Numpy array placing the list value to the arrays
    print(array)


# ****************************** 10. Quadratic Equation ************************************#
#  Purpose: Quadratic Equation
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   22-12-2018
#
# */

def Quadratic(a, b, c):  # Calling the Values
    determinant = b * b - 4 * a * c
    if determinant > 0:  # if determinant > 0 find the roots using formulas
        root1 = (-b + math.sqrt(determinant) / 2 * a)
        root2 = (-b + math.sqrt(determinant) / 2 * a)
    elif determinant == 0:
        root1 = root2 = -b / (2 * a)
        print("root1=root2=%.2f", root1)
    else:
        realpart = -b / (2 * a)
        imaginaryPart = math.sqrt(-determinant) / (2 * a)
        print("root1 = %.2f+%.2fi and root2 = %.2f-%.2fi", realpart, imaginaryPart, realpart, imaginaryPart)


# ****************************** 11. Triplets ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def Triplets(arr):
    x = len(arr)  # Calculating the Length of array
    for i in range(0, x - 2):  # Iterates the array 0 to n-2
        for j in range(i + 1, x - 1):  # Iterates the array i+1 to n-1
            for k in range(j + 1, x):  # Iterates the array j+1 to n
                if arr[i] + arr[j] + arr[k] == 0:  # Results gives 0 then satisfy the results
                    print("", arr[i], "", arr[j], "", arr[k])


# ****************************** 12.Euclidean Distance  ************************************#
#  Purpose: Find the Euclidean Distance
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   22-12-2018
#
# */
def Euclidean(x, y):
    a = (x * x) + (y * y)
    distance = math.pow(a, 0.5)
    print("Distance is", distance)


# ****************************** 13.StopWatch Timer  ************************************#
#  Purpose: Calculating the StopWatch
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */
start_timer = 0
stop_timer = 0
elapsed = 0


def Start1():
    Start1.start_timer = time.time()  # Calculating the Start Time
    print("Start Time is ", Start1.start_timer)


def Stop1():
    Stop1.stop_timer = time.time()  # Calculating the Stop Time
    print("Stop Time is", Stop1.stop_timer)


def Elapsedtime():  # Elapsed Time i,e Stop-Start
    # print(Start1.start_timer)
    # print(Stop1.stop_timer)
    elapsed = Stop1.stop_timer - Start1.start_timer
    print("Elapsed Timer is", elapsed)
    print("Converting Milliseconds to Seconds", (elapsed / 1000), "sec")


# ****************************** 14.Windchill  ************************************#
#  Purpose: Calculate the WindChill
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def Wind(temp, windSpeed):
    if (temp < 50 and (windSpeed > 3 and windSpeed < 120)):  # Checking the Condition
        windChill = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * math.pow(windSpeed,
                                                                               0.16)  # Calculate by using the formula
        print("WindChill is", windChill)
    else:
        print("Enter the Valid Input")


# ****************************** 15.Permutation of a String  ************************************#
#  Purpose: String Permutation
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   22-12-2018
#
# */

def permutation(
        s1):    # The length of the string is the base. So the permutations (with repetition) of 'abc' correspond to the numbers
    # from 0 to 3**3-1 in base 3, where 'a' is the digit 0, 'b' is 1 and 'c' is 2.

    base = len(s1)
    for n in range(base ** base):
        yield "".join(s1[n // base ** (base - d - 1) % base] for d in range(base))


# ************************************************* II Algorithm Problems ************************************#


# *********************************************** 1. String of Anagrams  ************************************#
#  Purpose: Determines whether Strings are Anagrams or Not
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   24-12-2018
#
# */
global str1
global str2


def Anagrams(str1, str2):  # Pass Strings
    word1 = str1  # Converting Strings to the List
    l1 = list(word1)
    word2 = str2
    l2 = list(word2)
    if (sorted(l1) == sorted(l2)):  # Comparing 2 Sorted List
        print("Strings are Anagram")
    else:
        print("String are Not Anagram")


# Anagrams(1,1)


# *********************************************** 2.Prime No. Check ****************************************#
#  Purpose: Check Whether a given no.are prime or not in the range
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   24-12-2018
#
# */

def get_prime():
    list = []
    is_prime = True
    for i in range(1001):
        if i == 0 or i == 1:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            list.append(i)
    return list




def PrimeCheck(no1, no2):  # Pass the No. from start till end
    flag = 0
    l = []
    print("Prime No.s in a Range", no1, "And ", no2)
    for i in range(no1, no2 + 1):  # Iterate no1 to no2(i=no1;i<no2+1;i++)
        for j in range(2, i):  # Iterate (j=2;j<i;j++)
            if (i % j == 0):  # No1 is divisible by 2, break
                flag = 0
                break
            else:
                flag = 1
        if (flag == 1):  # If its not divisible then append in the list
            l.append(i)

    print(l)


# def get_anagram_prime():
#     li=get_prime()
#     a=[]
#     index = 0
#     for i in range(0, len(li)):
#         originalfirst = li[index]
#         sortedfirst = ''.join(sorted(str(li[index])))
#         for j in range(index + 1, len(li)):
#             next = ''.join(sorted(str(li[j])))
#             print(next)
#             if sortedfirst == next:
#                 a.update({originalfirst: li[j]})
#                 print("dict = ", a)
#             index += 1
#
#         print(a)


def get_anagram_prime():
    x=get_prime()
    #print(x)
    x=[str(i) for i in x]
    ana=[]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if sorted(x[i])==sorted(x[j]):
                ana.append(x[i])
                ana.append(x[j])
    return ana

# *************************** 3. Check Whether the given Prime Nos in Pallindrome or Not****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   24-12-2018
#
# */
def get_palindrome_prime():

    store_prime = get_prime()
    s = ''
    store_palindrome_prime = []
    for i in store_prime:
        string = ''
        string = str(i)
        string1 = string
        count = -1
        reverse_string1 = ''

        for j in range(0, len(string1)):
            reverse_string1 += string1[count]
            count = count - 1

        string1 = ''
        if reverse_string1 == string:
            store_palindrome_prime.append(string)

    return store_palindrome_prime


# *************************** 4. Searching and Sorting ****************************************#
#  Purpose: Differenct Searching and Sorting Techniques
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   24-12-2018
#
# */

# ********************************I. Binary Search Integer*********************************

def BinaySearchInteger(n):  # Pass nth element
    Start1()
    flag = 1
    print("Enter the array elements")
    arr = [int(input()) for i in range(n)]  # Accepting the 1D array
    x = len(arr)
    key = int(input("Enter the Key to search"))
    start = 0
    end = x - 1
    arr.sort()  # Before Binary Search Sorting is done
    print("Sorted Array", arr)
    while (start <= end):  # Iterate from start less than end
        mid = (start + end) // 2  # Calculating a middle tera
        if (key == arr[mid]):  # If Key matches with middle than retrun key
            flag = 0
            print("Element is found at the location", mid)
        if (key < arr[mid]):  # If search key is less than middle than shikf to right
            end = mid - 1
        else:
            start = mid + 1  # Else Shift to the right
    if (flag == 1):
        print("Element Not Found")
        Stop1()
        Elapsedtime()


# ********************************II. Binary Search String  *********************************

def BinaySearchString(l, key):
    Start1()
    flag = 1
    x = len(l)
    start = 0
    end = x - 1
    l.sort()
    print("Sorted Array", l)
    while (start <= end):
        mid = (start + end) // 2
        if (key == l[mid]):
            flag = 0
            print("Element is found at the location", mid)
        if (key < l[mid]):
            end = mid - 1
        else:
            start = mid + 1
    if (flag == 1):
        print("Element Not Found")
    Stop1()
    Elapsedtime()


# ********************************III. Insertion Sort for Integer *********************************

def InsertionSortInteger(n):
    Start1()
    print("Enter the Elements in the array")
    arr = [int(input()) for i in range(n)]
    x = len(arr)
    for i in range(1, n):  # Iterate the values of array for a Insertion Sort
        j = i  # j=1
        temp = arr[i]  # temp=0th element
        while (j > 0 and temp < arr[j - 1]):  # Iterate till j greater than 0 and temp less than a[0]
            arr[j] = arr[j - 1]  # Swapping Values
            j = j - 1
        arr[j] = temp
    print("Sorting Elements are")
    for i in range(0, n):
        print(arr[i])
    Stop1()
    Elapsedtime()


# ********************************IV Insertion Sort for String *********************************

def InsertionSortString(n):
    Start1()
    print("Enter the Elements in the array")
    arr = [(input()) for i in range(n)]
    # x=len(arr)
    for i in range(1, n):
        j = i
        temp = arr[i]
        while (j > 0 and temp < arr[j - 1]):
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    print("Sorting Elements are")
    for i in range(0, n):
        print(arr[i])
    Stop1()
    Elapsedtime()


# ********************************V Bubble Sort for Integer*********************************
def BubbleSortInteger(n):
    print("Enter the Elements in the array")
    arr = [int(input()) for i in range(n)]
    for i in range(0, n - 1):  # Iterate i to 0 to n-1
        for j in range(0, n - i - 1):  # Iterate j to 0 to n-i-1(for getting the values of indexing)
            if (arr[j] > arr[j + 1]):  # Cheking is array of 0th element is greater than array of 1st element
                temp = arr[j]  # If Yes than Swap Values
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted Array is")
    for i in range(0, n):
        print(arr[i])
    Stop1()
    Elapsedtime()


# ********************************V Bubble Sort for String*********************************

def BubbleSortString(n):
    Start1()
    print("Enter the String Elements in the array")
    arr = [(input()) for i in range(n)]
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted Array is")
    for i in range(0, n):
        print(arr[i])
    Stop1()
    Elapsedtime()


# *************************** 4. Question Number Generation****************************************#
#  Purpose: Question Number Generation
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   26-12-2018
#
# */

def Search(low, high):  # Pass the Values as low and high
    if (high - low == 1):
        return low
    mid = low + (high - low) / 2  # Finding the Middle element
    print("Is Your Number Less then", mid, "Press 1 for Yes and 0 for No")
    y = int(input())  # Asking the Questions for a nos.
    if (y == 1):  # If y=1 then check for left side i,e for a low
        return Search(low, mid)
    elif (y == 0):  # If y=0 then check for Right side i,e for a Right
        return Search(mid, high)
    else:
        print("Valid Input")

    return 0


# *************************** 7. Insertion Sort Using String****************************************#
#  Purpose: Insertion Sort Using String
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 3.7
#  *  @since   26-12-2018
#
# */

def Insertion(str1):
    l = []  # Converting Str to the list
    l = list(str1)
    print(l)
    for i in range(len(l)):
        j = i
        temp = l[i]
        while (j > 0 and temp < l[j - 1]):
            l[j] = l[j - 1]
            j = j - 1
            l[j] = temp
    # str2 = ''.join(l)
    # str1=String(l)
    print("Sorting Elements are")
    for i in range(len(l)):
        print(l[i])


# *************************** 8. Bubble Sort ****************************************#
#  Purpose: Bubble Sort
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def Bubble(arr):
    l = []  # Converting Str to the list
    l = list(arr)
    print(l)
    for i in range(0, len(l) - 1):
        for j in range(0, len(l) - i - 1):
            if (l[j] > l[j + 1]):
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    print("Sorted Array is")
    for i in range(len(l)):
        print(l[i])


# *************************** 9. MergeSort****************************************#
#  Purpose: Program to implement Merge Sort
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def MergeSort1(lefthalf, righthalf, alist):
    i = 0
    j = 0
    k = 0
    while (i < len(lefthalf) and j < len(righthalf)):  # Iterate the loop for a left and right array...
        if lefthalf[i] < righthalf[j]:  # If left is less than right, then place the value of left array
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            alist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1

    print(alist)
    # for i in range(len(alist)):
    #     print(i)


def MergeSort(alist):  # Passing the List
    n = len(alist)
    lefthalf = []  # Creating Empty List of Left half
    righthalf = []  # Creating Empty List of Right half
    if (len(alist) < 2):
        return

    mid = len(alist) // 2  # Calculating the Middle Element
    for i in range(mid):  # Used the Loop for calculating the left Half, and append in a left
        lefthalf.append(alist[i])

    for i in range(mid, n):  # Used the Loop for calculating the Right Half, and append in a Right
        righthalf.append(alist[i])

    # lefthalf = alist[:mid]
    # righthalf = alist[mid+1:]

    MergeSort(lefthalf)  # Pass the results to the methods
    MergeSort(righthalf)
    MergeSort1(lefthalf, righthalf, alist)


# *************************** 10. Vending Machine****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */


def VendingMachine(money):
    try:
        notes = [1000, 500, 100, 50, 10, 5, 2, 1]
        total = 0
        countnotes = 0
        rem = 0
        while (money > 0):  # Iterate through Money>0
            for i in range(0, len(notes)):  # Should be work till notes are present and use
                if (money >= notes[i]):  # Checking the individual notes with the money
                    countnotes = money // notes[i]
                    rem = money % notes[i]
                    money = rem
                    total += countnotes
                    print(countnotes, "Notes of", notes[i])
            VendingMachine(money)
            print("Total No. of Notes", total)
    except RecursionError:
        print("")


# ***************************11. Days of a Week****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def DayofWeek(m, d, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    if (d0 == 0):
        print("Your Date is", d0, "and Day is Sunday:")
    elif (d0 == 1):
        print("Your Date is", d0, "and Day is Monday:")
    elif (d0 == 2):
        print("Your Date is", d0, "and Day is Tuedsay:")
    elif (d0 == 3):
        print("Your Date is", d0, "and Day is Wednesday:")
    elif (d0 == 4):
        print("Your Date is", d0, "and Day is Thursday")
    elif (d0 == 5):
        print("Your Date is", d0, "and Day is Friday::")
    elif (d0 == 6):
        print("Your Date is", d0, "and Day is Saturday")


# *************************** 12. Tempreature ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def temperaturConversion(fahrenheit, celsius):
    fahrenheit1 = (celsius * 9 / 5) + 32;
    print("Temperature in Fahrenheit is", fahrenheit1)
    celsius1 = (fahrenheit - 32) * 5 / 9;
    print("Temperature in Celsius is", celsius1)


# *************************** 13. Monthly Payement ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def Interest(principal_loan, rate, year):
    n = (12) * (year)
    r = (rate) / (1200)
    payement = (principal_loan * (r)) / (1 - math.pow(1 + r, -n))
    print("Monthly Payement is", float(payement))


# *************************** 14. Newton Method ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */
def Newton(no, t, epsilon):
    while (math.fabs(t - no / t) > epsilon * t):
        t = (no / t + t) / (2.0)
    print(t)


# ****************************15 & 16. Decimal to Binary****************************************#
#  Purpose: Program to implement Decmial,Binary,Swapping .
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   27-12-2018
#
# */
def ToBinary(str1):
    while (len(str1) != 8):  # Padding the elements with 0
        str1 = "0" + str1
    print(str1)

    mid = len(str1) / 2
    part1 = str1[:int(mid)]  # Slicing start till mid
    part2 = str1[int(mid):]  # Slicing mid to end
    print(part1)
    print(part2)
    new_str = part2 + part1
    print(new_str)
    # int(bn, 2)
    new_no = (int(new_str, 2))
    print("New Number is", new_no)
    if (isPowerOfTwo(new_no)):  # Checking if its power of 2
        print("Nos. is a power of 2")
    else:
        print("Nos. is Not a power of 2")


def Log2(x):
    return (math.log10(x) / math.log10(2));


def isPowerOfTwo(new_no):
    return (math.ceil(Log2(new_no)) == math.floor(Log2(new_no)));


# ****************************15 & 16. Decimal to Binary****************************************#
#  Purpose: Searching of a word from a file and sort
#  *
#  *  @author  Shahazad Shaikh
#  *  @version 1.0
#  *  @since   27-12-2018
#
# */
def file():
    filename = open("/home/admin1/Documents/Shahazad/myfile.txt", "r")
    # file_handle = open(filename, "r")
    words = []
    for line in filename:
        words += line.split()
        # filename.close()
        # words.sort()
    print(sorted(words))
    filename.close()
