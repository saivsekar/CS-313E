#  File: Tower.py

#  Description: Reads number of disks and outputs the number of moves needed to move all from source to destination peg, following rules of the Tower of Hanoi with four pegs

#  Student's Name: Reece Mathew

#  Student's UT EID: rtm2244

#  Partner's Name: Sai Chandrasekar

#  Partner's UT EID: svc439

#  Course Name: CS 313E 

#  Unique Number: 52535

#  Date Created: 10/14/2022

#  Date Last Modified: 10/14/2022

import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves(n):

    # Input: n the number of disks
    # Output: returns the number of transfers using three needles, only one spare between source and destination
    def one_spare_needle (n):
            if (n == 1):
                return 1
            else:
                return one_spare_needle (n - 1) + 1 + one_spare_needle (n - 1)

    # Input: n the number of disks
    # Output: returns the number of transfers using four needles
    def towers(n):
        # Calculates k value
        k = int(n - math.sqrt(2 * n + 1) + 1)
        # base cases
        if (n < 1):
            return 0
        if (n == 1):
            return 1
        if (n == 2):
            return 3
        
        else:
            # Steps 1 and 5 have two spare needles while Steps 2 and 4 have one spare needle
            return towers (k) + one_spare_needle (n - k - 1) + 1 + \
                one_spare_needle (n - k - 1) + towers (k)
            
    return towers(n) # function return for final output

def main():
    # read number of disks and print number of moves
    for line in sys.stdin:
        line = line.strip()
        num_disks = int(line)
        print(num_moves(num_disks))


if __name__ == "__main__":
    main()