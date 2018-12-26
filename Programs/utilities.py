import random
import math
import time
import numpy as np
import sys

sys.setrecursionlimit(1500)


class NumericException(RuntimeError):
    pass


def verify_digit():
    l5 = [0 - 9]
    for i in range(len(l5)):
        if str1 in l5:
            raise NumericException


def addition():
    a = 10
    b = 20
    c = a + b
    print(c)
    ############################################


# ****************************** 1.User Inputs************************************#
#  Purpose: Determines whether or not n is prime.
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */
def Uname(u_name):
    if len(u_name) > 3:
        print("The ActualName is", u_name)
        new_name = input("Enter the name to be change")
        if (len(new_name)):
            print("Hello", new_name, "How r u?")
        else:
            print("Enter the Valid Name")
    else:
        print("Wrong Input")


# ****************************** 2. Flip Coins  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def Flips(n):
    head = 0
    tails = 0
    for i in range(0, n):
        coins = random.randint(0, 1)
        if (coins < 0.5):
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
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */
def Leap(year):
    if ((year % 4 == 0) or (year % 400 == 0) and ((year % 100 != 0))):
        print("The Given Year is a Leap Year")
    else:
        print("The Given Year is Not the Leap Year")


# ****************************** 4. Power of 2 ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */

def Power(n):
    mul = 2;
    if n < 31:
        for i in range(1, n + 1):
            print("Power of the 2 is", 2 ** i)
    else:
        print("Overflows the Integer")


# ****************************** 5. Harmonic Number ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */

def Harmonic(n):
    h = 0
    for i in range(1, n):
        h = 1 / i
    print(h)

    # print(freq_sum/sum)


# ****************************** 6. Prime Nos Factorization ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */

def Prime(n):
    fact = 2
    for fact in range(fact, n):
        while (n % fact == 0):
            print(" Factor is", fact)
            n = n / fact
    # if(n>1):
    #   print("Factorial of a Number is", n)


# ****************************** 7. Gambler Program ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */
def Gambler(stakes, goals, trials):
    bets = wins = i = 0
    for i in range(i, trials):
        cash = stakes
        while (cash > 0 and cash < goals):
            bets += 1
            a = random.uniform(0, 1)
            if (a < 0.5):
                cash += 1
            else:
                cash = cash - 1
        if (cash == goals):
            wins += 1
    print(wins, "Wins of", trials)
    print("Percentage of Game Wins", 100.0 * wins / trials)
    print("Average of Bets", 1.0 * bets / trials)


# ****************************** 8. Coupon Numbers ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   06-08-2017
#
# */

def Coupon(coupon_no):
    l = []
    count = 0
    l = [int(i) for i in str(coupon_no)]
    print(l)
    while (len(l) > 0):
        number = random.randint(0, 9)
        count += 1
        if (number in l):
            l.remove(number)
            print(l)

    print("Total random numbers to generate coupoun", count)


# ****************************** 9. 2D Array  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def Twoarray(m, n):
    matrix = [[0 for j in range(m)] for i in range(n)]
    print(matrix)

    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(input("Enter the Array Elements"))

    array = np.array(matrix)
    print(array)


# ****************************** 10. Quadratic Equation ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def Quadratic(a, b, c):
    determinant = b * b - 4 * a * c
    if (determinant > 0):
        root1 = (-b + math.sqrt(determinant) / 2 * a)
        root2 = (-b + math.sqrt(determinant) / 2 * a)
    elif (determinant == 0):
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
    found = None
    #  a=bool(found)
    x = len(arr)
    for i in range(0, x - 2):
        for j in range(i + 1, x - 1):
            for k in range(j + 1, x):
                if (arr[i] + arr[j] + arr[k] == 0):
                    # print("", arr[i])
                    # print("", arr[j])
                    # print("", arr[k])
                    print("", arr[i], "", arr[j], "", arr[k])
                #  a=true


# ****************************** 12.Euclidean Distance  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */
def Euclidean(x, y):
    a = (x * x) + (y * y)
    distance = math.pow(a, 0.5)
    print("Distance is", distance)


# ****************************** 13.StopWatch Timer  ************************************#
#  Purpose: Determines whether Leap Year or Not
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
    Start1.start_timer = time.time()
    print("Start Time is ", Start1.start_timer)


def Stop1():
    Stop1.stop_timer = time.time()
    print("Stop Time is", Stop1.stop_timer)


def Elapsedtime():
    # print(Start1.start_timer)
    # print(Stop1.stop_timer)
    elapsed = Stop1.stop_timer - Start1.start_timer
    print("Elapsed Timer is", elapsed)
    print("Converting Milliseconds to Seconds", (elapsed / 1000), "sec")


# ****************************** 14.Windchill  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def Wind(temp, windSpeed):
    if (temp < 50 and (windSpeed > 3 and windSpeed < 120)):
        windChill = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * math.pow(windSpeed, 0.16)
        print("WindChill is", windChill)
    else:
        print("Enter the Valid Input")


# ****************************** 14.Permutation of a String  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def permutation(
        s1):  ## The length of the string is the base. So the permutations (with repetition) of 'abc' correspond to the numbers
    # from 0 to 3**3-1 in base 3, where 'a' is the digit 0, 'b' is 1 and 'c' is 2.

    base = len(s1)
    for n in range(base ** base):
        yield "".join(s1[n // base ** (base - d - 1) % base] for d in range(base))


# ************************************************* II Algorithm Problems ************************************#


# *********************************************** 1. String of Anagrams  ************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */
global str1
global str2


def Anagrams(str1, str2):
    word1 = str1
    l1 = list(word1)
    # l1.sort()
    word2 = str2
    l2 = list(word2)
    # l2.sort()
    if (sorted(l1) == sorted(l2)):
        print("Strings are Anagram")
    else:
        print("String are Not Anagram")


# Anagrams(1,1)


# *********************************************** 2.Prime No. Check****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def PrimeCheck(no1, no2):
    flag = 0
    l = []
    print("Prime No.s in a Range", no1, "And ", no2)
    for i in range(no1, no2 + 1):
        for j in range(2, i):
            if (i % j == 0):
                flag = 0
                break
            else:
                flag = 1
        if (flag == 1):
            l.append(i)
            pallindrome(i)
    print(l)


# *************************** 3. Check Whether the given Prime Nos in Pallindrome or Not****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

def pallindrome(n):
    x = []
    n1 = str(n)
    a = n1[::-1]
    if (a == n1):
        x.append(a)
        print("Given Nos. is Pallindrome", x)

    else:
        print("Not the Pallindrome Nos")
    print(x)


# *************************** 4. Searching and Sorting ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   22-12-2018
#
# */

# ********************************I. Binary Search Integer*********************************

def BinaySearchInteger(n):
    Start1()
    flag = 1
    print("Enter the array elements")
    arr = [int(input()) for i in range(n)]
    x = len(arr)
    key = int(input("Enter the Key to search"))
    start = 0
    end = x - 1
    arr.sort()
    print("Sorted Array", arr)
    while (start <= end):
        mid = (start + end) // 2
        if (key == arr[mid]):
            flag = 0
            print("Element is found at the location", mid)
        if (key < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    if (flag == 1):
        print("Element Not Found")
        Stop1()
        Elapsedtime()


# ********************************II. Binary Search String  *********************************

def BinaySearchString(n):
    Start1()
    flag = 1
    print("Enter the String array elements")
    arr = [(input()) for i in range(n)]
    x = len(arr)
    key = (input("Enter the Key to search"))
    start = 0
    end = x - 1
    arr.sort()
    print("Sorted Array", arr)
    while (start <= end):
        mid = (start + end) // 2
        if (key == arr[mid]):
            flag = 0
            print("Element is found at the location", mid)
        if (key < arr[mid]):
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
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def Search(low, high):
    if (high - low == 1):
        return low
    mid = low + (high - low) / 2
    print("Is Your Number Less then", mid, "Press 1 for Yes and 0 for No")
    y = int(input())
    if (y == 1):
        return Search(low, mid)
    elif (y == 0):
        return Search(mid, high)
    else:
        print("Valid Input")

    return 0


# *************************** 7. Insertion Sort Using String****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def Insertion(str1):
    l = []
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


# *************************** 7. Bubble Sort Using String****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def Bubble(arr):
    l = []
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


# *************************** 7. MergeSort****************************************#
#  Purpose: Determines whether Leap Year or Not
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
    while (i < len(lefthalf) and j < len(righthalf)):
        if lefthalf[i] < righthalf[j]:
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


def MergeSort(alist):
    n = len(alist)
    #alist = []
    #alist = list(arr)
    # print(alistl)
    # print("Splitting ", alist)
    lefthalf=[]
    righthalf=[]
    if (len(alist) < 2):
        return

    mid = len(alist) // 2
    for i in range(mid):
        lefthalf.append(alist[i])

    for i in range(mid,n):
        righthalf.append(alist[i])

    # lefthalf = alist[:mid]
    # righthalf = alist[mid+1:]


    MergeSort(lefthalf)
    MergeSort(righthalf)
    MergeSort1(lefthalf, righthalf, alist)


#  print("Merging ", alist)"""

# *************************** 7. Vending Machine****************************************#
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
        countnotes=0
        rem=0
        while(money>0):
            for i in range(0,len(notes)):
                if(money >= notes[i]):
                    countnotes = money // notes[i]
                    rem = money % notes[i]
                    money = rem
                    total += countnotes
                    print(countnotes,"Notes of", notes[i])
            VendingMachine(money)
            print("Total No. of Notes", total)
    except RecursionError:
        print("")

# *************************** 7. Days of a Week****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def DayofWeek(m,d,y):
    ls = ['sunday', 'monday', 'tuedsay', 'wednesday', 'thrusdar', 'friday', 'saturday']
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    if (d0==0):
        print("Your Date is", d0, "and Day is Sunday:")
    elif(d0 == 1):
        print("Your Date is", d0, "and Day is Monday:")
    elif(d0 == 2):
        print("Your Date is", d0, "and Day is Tuedsay:")
    elif(d0 == 3):
        print("Your Date is", d0, "and Day is Wednesday:")
    elif(d0== 4):
        print("Your Date is", d0, "and Day is Thursday")
    elif(d0 == 5):
        print("Your Date is", d0, "and Day is Friday::")
    elif(d0 == 6):
        print("Your Date is", d0, "and Day is Saturday")


# *************************** 7. Tempreature ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def temperaturConversion(fahrenheit,celsius):
    fahrenheit1=(celsius*9/5)+32;
    print("Temperature in Fahrenheit is" ,fahrenheit1)
    celsius1 = (fahrenheit - 32) * 5 / 9;
    print("Temperature in Celsius is" , celsius1)


# *************************** 7. Monthly Payement ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */

def Interest(principal_loan,rate,year):
    n=(12)*(year)
    r=(rate)/(1200)
    payement=(principal_loan*(r))/(1-math.pow(1+r,-year))
    print("Monthly Payement is", float(payement))



# *************************** 7. Newton Method ****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */
def Newton(no,t,epsilon):
    while(math.fabs(t-no/t)>epsilon*t):
        t=(no/t+t)/(2.0)
    print(t)

# *************************** 7. Decimal to Binary****************************************#
#  Purpose: Determines whether Leap Year or Not
#  *
#  *  @author  BridgeLabz
#  *  @version 1.0
#  *  @since   26-12-2018
#
# */
