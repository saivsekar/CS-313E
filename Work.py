#  File: Work.py

#  Description: Help out Vyasa figure out the optimal coffee
#  to code ratio

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/27/23

#  Date Last Modified: 9/28/23

import sys
import time

# Input: int v, the number of lines that must be written
#           before the first cup of coffee
#        int k, the productivity factor
# Output: int sum, the number of lines of code written in total

def getsum(v,k):
    sum = v
    p = 1
    checker = 1

    while(checker > 0): # Vyasa falls asleep when checker hits zero
        checker = v // (k**p)
        p += 1
        sum += checker
    return sum


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee

def linear_search(n: int, k: int) -> int:
    # use linear search here
    for i in range(1, n+1):  # starts at zero bc Vyas would fail if he wrote nothing
        if( getsum(i,k) >= n):
            return i 
    return i


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee


def binary_search(n: int, k: int) -> int:
    low = 0
    lowsum = getsum(low,k)
    high = n
    highsum = getsum(high,k)

    while ( high >= low ):
        # initializes interval midpoint and number of lines of code
        mid = (low+high)//2
        midsum = getsum(mid, k)
        
        # break point
        if(midsum == n):
            return mid
        
        # middle is the new low if sum is too small
        if (midsum < n):   
            low = mid + 1   # '+ 1' added because if uses '<' instead of '<='
        # middle is the new high if sum is too big
        if(midsum > n):
            high = mid - 1   # '+ 1' added because if uses '<' instead of '<='

    return low
    
    
# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
