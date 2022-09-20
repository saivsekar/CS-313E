#  File: Poker.py

#  Description: Simulates a regular Poker game otherwise known as the 5-Card Draw

#  Student's Name: Reece Mathew

#  Student's UT EID: rtm2244

#  Partner's Name: Sai Chandrasekar

#  Partner's UT EID: svc439

#  Course Name: CS 313E 

#  Unique Number: 52535

#  Date Created: 9/17/22

#  Date Last Modified: 9/18/22

import sys, random

class Card (object):

    # 11 - Jack, 12 - Queen, 13 - King, 14 - Ace
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    
    # Clubs, Diamonds, Hearts, Spades
    SUITS = ('C', 'D', 'H', 'S')
    

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
      if (rank in Card.RANKS):
          self.rank = rank
      else:
          self.rank = 12

      if (suit in Card.SUITS):
          self.suit = suit
      else:
          self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object):
    # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append (card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)

    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range (num_players):
            hand = []
            for j in range (self.numCards_in_Hand):
                hand.append (self.deck.deal())
            self.players_hands.append (hand)

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        print()

        # determine the type of each hand and print
        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand
        points = [0] * 10 # create a list to store possible points for each hand
        hands = ["NA"] * 10 # create a list to store possible handtypes for each hand

        for i in range(len(self.players_hands)):
            
            # create a list of possible points/hands for each possible player hand
            points[0], hands[0] = self.is_royal(self.players_hands[i])
            points[1], hands[1] = self.is_straight_flush(self.players_hands[i])
            points[2], hands[2] = self.is_four_kind(self.players_hands[i])
            points[3], hands[3] = self.is_full_house(self.players_hands[i])
            points[4], hands[4] = self.is_straight(self.players_hands[i])
            points[5], hands[5] = self.is_three_kind(self.players_hands[i])
            points[6], hands[6] = self.is_two_pair(self.players_hands[i])
            points[7], hands[7] = self.is_one_pair(self.players_hands[i])
            points[8], hands[8] = self.is_high_card(self.players_hands[i])
            points[9], hands[9] = self.is_royal(self.players_hands[i])

            maxpoints = max(points)  # gets largest point value for hand
            indx = hands.index(maxpoints) # get index of largest point value
            maxhand = hands[indx]   # create container to hold maximum hand object

            hand_type.append(maxhand)   
            hand_points.append(maxpoints)  

        for i in range(len(hand_type)):
            print('Player ' + str(i + 1) + ' : ' + str(hand_type[i]))
        print()

        # determine winner and print
        maxi = max(hand_points)             #get max point value
        ind = hand_points.index(maxi)       #get index of winning hand
        winning_type = hand_type[ind]       #get hand type of winning hand

        if hand_type.count(winning_type) > 1:   # deals with Ties
            indices = []
            for i in range(len(hand_type)):
                if hand_type[i] == winning_type:
                    indices.append([hand_points[i], i])
            indices = sorted(indices, reverse=True)
            for i in range(len(indices)):
                print('Player ' + str(indices[i][1] + 1) + ' ties.')
        else:
            player_index = hand_type.index(winning_type)
            print('Player ' + str(player_index + 1) + ' wins.')

    
    def is_high_card (self,hand):
            points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)

            return points, 'High Card'
    
    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair (self, hand):
        one_pair = False
        for i in range (len(hand) - 1):
            # checks each pair of cards for similarity
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                pop1 = hand[i]
                pop2 = hand[i + 1]
                hand.pop(i)
                hand.pop(i)
                hand.insert(0, pop1)
                hand.insert(1, pop2)
                break # all found pairs are inserted into 
                      # the beginning of hand 

        if (not one_pair):
            return 0, ''

        points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'One Pair'

    def is_two_pair (self, hand):
        two_pair = False
        cnt = 0 # variable to count number of pairs found
        for i in range(len(hand)-1):
            # checks each pair of cards for similarity
            if (hand[i] == hand[i+1]):
                cnt +=1 
                if( cnt ==1 ):
                    # creates variable to hold first pair
                    firstpair = hand[i] 
                if( cnt == 2 ):
                    # creates variable to hold second pair
                    secondpair = hand[i]

        # after 2 pairs are found, boolean is confirmed
        # and pairs are removed from hand
        if cnt >= 2: 
            two_pair = True
            for i in range(2):
                hand.remove(firstpair)
                hand.remove(secondpair)

        
            
        if (not two_pair):
            return 0, ''

        points = 3 * 15 ** 5 + (firstpair.rank) * 15 ** 4 + (firstpair.rank) * 15 ** 3
        points = points + (secondpair.rank) * 15 ** 2 + (secondpair.rank) * 15 ** 1
        points = points + (hand[0].rank)

        return points, 'Two Pair'

    def is_three_kind (self, hand):
        three_kind = False

        # if/elif block goes through the only possible 3-kind situations
        if (hand[0].rank == hand[1].rank == hand[2].rank):
            three_kind = True
        elif (hand[1].rank == hand[2].rank == hand[3].rank):
            three_kind = True
            pop = hand[0]
            hand.pop(0)
            hand.insert(3, pop)
        elif (hand[2].rank == hand[3].rank == hand[4].rank):
            three_kind = True
            pop1 = hand[0]
            pop2 = hand[1]
            hand.pop(0)
            hand.pop(0)
            hand.append(pop1)
            hand.append(pop2)

        if (not three_kind):
            return 0, ''

        points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Three of a Kind'

    def is_straight (self, hand):
        rank_order = True
        for i in range(len(hand)-1):  # checks each pair for continuity of straight
            rank_order = rank_order and (hand[i].rank == (hand[i + 1].rank + 1))
        
        if (not rank_order):
          return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    def is_flush (self, hand):
        same_suit = True

        #checks that all-same-suit condition is satisfied
        for i in range (len(hand) - 1): 
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'

    def is_full_house (self, hand):
        full_house = False

        #checks for the only 2 possible full house situations
        if (hand[0].rank == hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank):
            full_house = True
        elif (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank == hand[4].rank):
            full_house = True
            hand[0], hand[1], hand[3], hand[4] = hand[3], hand[4], hand[0], hand[1]

        if (not full_house):
            return 0, ''

        points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Full House'

    def is_four_kind (self, hand):
        four_rank = False
        # checks for only possible 4-kind situations
        if hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank:
            four_rank = True
        elif hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank:
            four_rank = True
            hand[0], hand[4] = hand[4], hand[0]

        if (not four_rank):
            return 0, ''

        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Four of a Kind'

    def is_straight_flush (self, hand):
      same_suit = True
      # checks that all card objects share 1 suit
      for i in range (len(hand) - 1):
        same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

      if (not same_suit):
        return 0, ''

      rank_order = True
      # checks for continuity of straight card objects
      for i in range (len(hand)-1):
          rank_order = rank_order and ( (hand[i].rank -1) == (hand[i + 1].rank) )
      
      if (not rank_order):
        return 0, ''

      points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'Straight Flush'

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal (self, hand):
      same_suit = True
      for i in range (len(hand) - 1):
        same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

      if (not same_suit):
        return 0, ''

      rank_order = True
      for i in range (len(hand)):
        rank_order = rank_order and (hand[i].rank == 14 - i)

      if (not rank_order):
        return 0, ''

      points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

      return points, 'Royal Flush'

    

def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker (num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()
