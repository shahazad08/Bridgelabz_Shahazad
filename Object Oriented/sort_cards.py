Conversation
opened.
1
unread
message.

Skip
to
content
Using
Gmail
with screen readers
1
of
742
Fwd:
Inbox
x
Nikhil
Lad

6: 02
PM(48
minutes
ago)

to
me

---------- Forwarded
message - --------
From: Nikhil
Lad < nikhillad01 @ gmail.com >
Date: Thu, Jan
10, 2019
at
5: 58
PM
Subject:
To: Janhavi
Mhatre < janhavimhatre01 @ gmail.com >, Pushkar
Ishware < pushkar.ishware @ gmail.com >

"""******************************************************************************
* Purpose: Deck of Cards 2 Using Queue.
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 9-1-2018

******************************************************************************
"""

import random
import numpy as np
from DSA import DSA_Utilities


class DeckOfCards:
    """This class is used to write logic for deck of cards"""

    def shuffle(self):

        """Method to distribute 9 cards to 4 users"""

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11 Jack", "12 Queen", "13 King", "14 Ace"]

        list_cards = []  # list to hold cards.

        while len(list_cards) < 36:  # loop will run till 36 because we want to distribute 36 cards to 4 players.
            for i in range(0, 9):  # used to get only  9 numbers

                random_no = random.randint(1, 13)  # generate random number within 1 and 13

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)  # generates random number for suits.
                cards_rank = cards_rank + ' ' + suits[random_no_suits]  # adds suit and Rank together.

                if list_cards.__contains__(
                        cards_rank) is False:  # if list of cards does not contains cards_rank already:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)  # append cards_rank to list of cards

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # list comprehensions for matrix.
        index = 0
        for i in range(row):  # row iteration

            for j in range(column):  # column iteration .
                two_d_array[i][j] = list_cards[index]
                index += 1
        # print(two_d_array)
        a = np.array(two_d_array)
        print(a)
        # print("list of cards , : ",list_cards)
        limit = 9
        l1 = []  # four lists are used  for slicing of 36  elements in 4 parts(9 each).
        l2 = []
        l3 = []
        l4 = []
        # print("listttttt",list_cards)
        # print(list_cards[:9])
        for i in list_cards[0:9]:
            i = tuple((int(i[:2]), i[
                                   2:]))  # because we are getting data like ['12 Queen Spades']. all in string format so we split first two chars converts it to int and  add in tuple which makes to separate elements in one small tuple.
            # also it makes the sorting easy  with Int.

            l1.append(i)  # appends data to list.

        # l1.sort()
        l1.sort()  # sorts the data.
        print()
        print("Queue data")
        print()
        print("Player 1 Cards")

        for j in l1:
            q1.enqueue(j)  # adds data of player 1 to queue 1.

        # utilities.bubble_sort(l1)

        q1.show()
        # print("List data")
        # print(l1)
        print()

        for i in list_cards[9:18]:
            i = tuple((int(i[:2]), i[2:]))
            l2.append(i)
        l2.sort()
        print("Player 2 Cards")
        for l in l2:
            q2.enqueue(l)  # adds data of player 2 to queue 2.
        q2.show()
        print()

        for i in list_cards[18:27]:
            i = tuple((int(i[:2]), i[2:]))
            l3.append(i)
        l3.sort()
        print("Player 3 Cards")
        for m in l3:
            q3.enqueue(m)  # adds data of player 3 to queue 3.
        q3.show()
        print()

        for i in list_cards[27:]:
            i = tuple((int(i[:2]), i[2:]))
            l4.append(i)

        l4.sort()
        print("Player 4 Cards")
        for n in l4:
            q4.enqueue(n)  # adds data of player 4 to queue 4.
        q4.show()
        # print("First two chars : ",l1[8][:2])
        # s ="13 King Diamonds"
        # s2=tuple((int(s[:2]),s[2:]))
        # print(s2)
        return list_cards, two_d_array


q1 = DSA_Utilities.Queue()  # Queue class objects.
q2 = DSA_Utilities.Queue()
q3 = DSA_Utilities.Queue()
q4 = DSA_Utilities.Queue()

card = DeckOfCards()
card.shuffle()

# import random
# from functools import total_ordering
#
# graveyard = []
#
#
# @total_ordering
# class Card(object):
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         return '%s of %s' % (self.rank,
#                              self.suit)
#
#     def __repr__(self):
#         return str(self)
#
#     def num_rank(self, rank):
#         if rank[0] == "10":
#             return 10
#         if rank[0] == "A":
#             return 14
#         if rank[0] == "J":
#             return 11
#         if rank[0] == "Q":
#             return 12
#         if rank[0] == "K":
#             return 13
#         return int(rank)
#
#     def __lt__(self, other):
#         t1 = self.suit, self.num_rank(self.rank)
#         t2 = other.suit, self.num_rank(other.rank)
#         return t1 < t2
#     #
#     # def __gt__(self, other):
#     #     t1 = self.suit, self.rank
#     #     t2 = other.suit, other.rank
#     #     return t1 > t2
#
#
# class Deck(object):
#     def __init__(self):
#         pass
#
#     def __init__(self):
#         self.rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#         self.suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#         self.deck = [Card(r, s) for r in self.rank for s in self.suit]
#         random.shuffle(self.deck)
#
#     # def __getitem__(self, item):
#     #     return self.deck[item]
#
#     def fan(self):
#         for card in self.deck:
#             print(card)
#
#     def order(self):
#         return self.deck.sort()
#
#     def printGraveyard(self):
#         for dead in graveyard:
#             print(dead)
#
#     def player(self):
#         a = self.deck
#         print(a)
#         l1 = l2 = l3 = l4 = []
#         print("For Player 1")
#         l1 = a[:9]
#         print(l1)
#         print("\n")
#
#         print("For Player 2")
#         l2 = a[9:18]
#         print(l2)
#         print("\n")
#
#         print("For Player 3")
#         l3 = a[18:27]
#         print(l3)
#         print("\n")
#
#         print("For Player 4")
#         l4 = a[27:36]
#         print(l4)
#
#
# #    print(l4)
# #
#
#
# d = Deck()
# d.order()
# d.fan()
# d.player()
#
# # from Utilities import utilities
# # from Utilities import datastructure
# # suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
# # Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
# #
# # list_cards = []
# # def shuffle(self):
# #     card_suits = ''
# #     while len(list_cards) < 36:
# #         for i in range(0, 9):
# #             cards_rank = ''
# #             random_no = random.randint(1, 13)
# #             cards_rank = Rank[random_no - 1]
# #             random_no_suits = random.randint(0, 3)
# #             cards_rank = cards_rank + ' ' + suits[random_no_suits]
# #             if list_cards.__contains__(cards_rank) is False:
# #                 if len(list_cards) is not 36:
# #                     list_cards.append(cards_rank)
# #                     #print(cards_rank)
# #
# #     row = 4
# #     column = 9
# #     two_d_array = [[0 for j in range(column)] for i in range(row)]
# #     index = 0
# #     for i in range(row):
# #         for j in range(column):
# #             two_d_array[i][j] = list_cards[index]
# #             index += 1
# #
# #
# #     a = np.array(two_d_array)
# #     print(a)
# #     print("\n")
# #
# #     def num_rank(Rank):
# #         if Rank[0] == "A":
# #             return 14
# #         if Rank[0] == "J":
# #             return 11
# #         if Rank[0] == "Q":
# #             return 12
# #         if Rank[0] == "K":
# #             return 13
# #         #return int(Rank)
# #         print(Rank)
# #
# #     l1 = l2 = l3 = l4 = []
# #     print("For Player 1")
# #     l1=list_cards[:9]
# #     l1.sort()
# #     print(l1)
# #     print("\n")
# #
# #     print("For Player 2")
# #     l2=list_cards[9:18]
# #     print(l2)
# #     print("\n")
# #
# #     print("For Player 3")
# #     l3=list_cards[18:27]
# #     print(l3)
# #     print("\n")
# #
# #     print("For Player 4")
# #     l4 = list_cards[27:36]
# #     print(l4)
# #
# #     def __init__(self, list_cards, utility_obj, queue):
# #         self.list_cards = list_cards
# #         self.utility_obj = utility_obj
# #         self.queue = queue
# #
# #     def replacing(self):
# #         i = 0
# #         while i < len(self.list_cards):
# #             if bool(re.search('Ace', self.list_cards[i])):
# #                 self.list_cards[i] = re.sub('Ace', '14', self.list_cards[i], 1)
# #
# #             if bool(re.search('Jack', self.list_cards[i])):
# #                 self.list_cards[i] = re.sub('Jack', '11', self.list_cards[i], 1)
# #
# #             if bool(re.search('Queen', self.list_cards[i])):
# #                 self.list_cards[i] = re.sub('Queen', '12', self.list_cards[i], 1)
# #
# #             if bool(re.search('King', self.list_cards[i])):
# #                 self.list_cards[i] = re.sub('King', '13', self.list_cards[i], 1)
# #
# #             i += 1
# #
# #         ranks = []
# #         number = []
# #         i = 0
# #         while i < len(self.list_cards):
# #             ranks.append(self.list_cards[i].split(" "))
# #
# #             number.append(int(ranks[i][0]))
# #             i += 1
# #
# #         number = utilities.BubbleSortInteger(number)
# #         i = 0
# #         sorted_card = []
# #         suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
# #
# #         while i < 36:
# #
# #             string = ''
# #             random_no = random.randint(0, 3)
# #             string = suits[random_no]
# #             string = str(number[i]) + " " + string
# #
# #             while sorted_card.__contains__(string) is True:
# #                 random_no = random.randint(0, 3)
# #                 string = suits[random_no]
# #                 string = str(number[i]) + ' ' + string
# #
# #             if sorted_card.__contains__(string) is False:
# #                 sorted_card.append(string)
# #
# #             i += 1
# #
# #             i = 0
# #             while i < len(sorted_card):
# #
# #                 if bool(re.search('14', sorted_card[i])):
# #                     sorted_card[i] = re.sub('14', 'Ace', sorted_card[i], 1)
# #
# #                 if bool(re.search('11', sorted_card[i])):
# #                     sorted_card[i] = re.sub('11', 'Jack', sorted_card[i], 1)
# #
# #                 if bool(re.search('12', sorted_card[i])):
# #                     sorted_card[i] = re.sub('12', 'Queen', sorted_card[i], 1)
# #
# #                 if bool(re.search('13', sorted_card[i])):
# #                     sorted_card[i] = re.sub('13', 'King', sorted_card[i], 1)
# #
# #                 i += 1
# #
# #         player_objs = []
# #         limit = 0
# #         index = 9
# #         for i in range(0, 4):
# #             player_objs.append(card.shuffle, utilities, Queue)
# #
# #             for sorted_cards in sorted_card:
# #                 if limit < index:
# #                     player_objs[i].queue.enqueue(sorted_card[limit])
# #
# #                     limit += 1
# #             index += 9
# #
# #         for i in range(0, 4):
# #             print('Player', i + 1, '\n', '----------')
# #             print(player_objs[i].queue.show())
# #
# #
# # print('\n')
# #
# # #     def num_rank(Rank):
# # #         if Rank[0] == "A":
# # #             return 14
# # #         if Rank[0] == "J":
# # #             return 11
# # #         if Rank[0] == "Q":
# # #             return 12
# # #         if Rank[0] == "K":
# # #             return 13
# # #         return int(Rank)
# # # #
# #
# #
# # # print("\n")
# # # print(list_cards)
# # # while len(list_cards) < 36:
# # #     for i in range(0, 9):
# # #         s=[cards_rank[i]]
# # #         s.sort()
# # #     print(s)
# #
# #
# # # print(list_cards)
# # #
# #
# # shuffle(self=None)
