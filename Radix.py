
#  File: Radix.py

#  Description: Utilize Queues to implement Radix sort

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/21

#  Date Last Modified: 10/24

import sys


class Queue (object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))



# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings

def radix_sort(a):
    # create list of 36 queues
    # 26 letters + 10 numerals
    queues = []
    for i in range(37):
        queues.append(Queue())

    # -------------------------------------------------

    # initialize char dictionary with padding constant #
    val_dict = {'#': 0}

    # Populate dictionary containing key-value pairs with ordering based on ascii 
    # Hierarchy is preserved. We could've done it the ugly way (manually) but loops are ELEGANTTTT
    for i in range(1, 37):
        if (i <= 10):
            char = chr(47+i)
            val_dict[char] = i
        else:
            char = chr(86+i)
            val_dict[char] = i

    # -------------------------------------------------

    # Get length of string with most 'digits' (len)
    max = len( a[0] )
    for str in a:
        if ( len(str) > max):
            max = len(str)

    # -------------------------------------------------

    # Bring all strings to match length of longest string
    padded = []
    for str in a:
        while ( len(str) < max):
            str += '#'
        padded.append(str)

    # -------------------------------------------------

    # Here the Radix sort algorithm is implemented
    # ELEGANTTTTTT
    
    finalorder = padded
    for i in range (-1, -1*(max + 1), -1):

        # adds str values to queues in order
        for str in finalorder:
            queues[ val_dict[ str[i] ] ].enqueue(str)

        # dequeues str values in order
        # finalorder is wiped everyloop to dequeue values without weird collisions
        # also it's easier
        finalorder = []
        for j in queues:
            while ( not (j.is_empty())):
                finalorder.append ( j.dequeue() )

    # -------------------------------------------------

    # Take out added #'s and make string normal again
    for i in range ( len (finalorder)):
        currstring = finalorder[i]
        finalorder[i] = currstring.replace('#', '')

    # -------------------------------------------------


    return finalorder


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    # print the sorted_list
    print(radix_sort(word_list))
   
if __name__ == "__main__":
  main()
