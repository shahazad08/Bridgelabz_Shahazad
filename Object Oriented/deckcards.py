"""
******************************************************************************
* Purpose:  Deck Cards printing in a 2d array, and sort
*
* @author:  Shahazad Shaikh
* @version: 3.7
*
******************************************************************************
"""
import random
import numpy as np
from Utilities import utilities
import re
from Utilities.datastructure import *
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


list_cards = []
def shuffle(self):
    card_suits = ''
    while len(list_cards) < 36:                 # List of cards should not more than 36
        for i in range(0, 9):                   # Creating a list for a 0 to 9 individually
            cards_rank = ''
            random_no = random.randint(1, 13)   # Generation of a random number from 1 to 13
            cards_rank = Rank[random_no - 1]    # For calculating the rank, placed the no. in a cards rank
            random_no_suits = random.randint(0, 3) # As we have to distribute among 4
            cards_rank = cards_rank + ' ' + suits[random_no_suits] # Distributing a No. of cards anf a suits
            # in a cards rank
            if list_cards.__contains__(cards_rank) is False: # if cards not contain in a list,
                if len(list_cards) is not 36:               # add it to the list and not more than 36
                    list_cards.append(cards_rank)

    row = 4
    column = 9
    two_d_array = [[0 for j in range(column)] for i in range(row)]      # Calculating for a 2d array,
    index = 0
    for i in range(row):        # Placing a 2d cards in a row*column format
        for j in range(column):
            two_d_array[i][j] = list_cards[index]
            index += 1

    a = np.array(two_d_array)       # Use numpy to print in a 2d
    print("List Cards are",a)


   # print(a)

    queue = Queue()     # Intialize the Queue
    l1 = l2 = l3 = l4 = []  # create an empty list
    print("For Player 1")
    l1=list_cards[:9]       # Slicing from a list cards 1st 9 elements
    l1.sort()               # Sorting the list
    for a1 in l1:           # place a list1 elements in a a1
        queue.enqueue(l1)   # place a1 list to queue
        print(a1)           # print queue
    print("\n")

    print("For Player 2")  # Same for all players
    l2=list_cards[9:18]
    l2.sort()
    for a2 in l2:
        queue.enqueue(l2)
        print(a2)
    print("\n")

    print("For Player 3")
    l3=list_cards[18:27]
    l3.sort()
    for a3 in l3:
        queue.enqueue(l3)
        print(a3)
    print("\n")

    print("For Player 4")
    l4 = list_cards[27:36]
    l4.sort()
    for a4 in l4:
        queue.enqueue(l4)
        print(a4)

shuffle(self=None)

# for i in Rank:
#     if i == "Jack":
#         i = re.sub("Jack", "11", i)
#         print(i)