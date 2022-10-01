#  File: Palindrome.py

#  Description: Get smallest palindrome possible from input string 

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/29

#  Date Last Modified: 9/30

import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    n = len(str)

    # single letters are always palindromes
    if (n == 1):
        return str

    # converts strings to iterable lists
    normal = list(str)
    reverse = list(str[::-1])

    # initialize extra char array and index var
    xtra = []
    revidx = 0
    
    # goes through reversed string and appends
    #   each extra char to array till matching
    #   chars appear 
    while( normal[0] != reverse[revidx] ):
        xtra.append(reverse[revidx])
        revidx += 1
    
    xtra = ''.join(xtra)
    
    return xtra + str




# Input: no input
# Output: a string denoting all test cases have passed

def test_cases():
    # write your own test cases
    a = 'sasce'
    b = 'quoro'
    assert smallest_palindrome(a) == 'ecsasce'
    assert smallest_palindrome(b) == 'orouquoro'

    return "all test cases passed"


def main():
    # run your test cases
    '''
    print (test_cases())    # test cases not run bc autograder doesn't allow for it
    '''

    # read the data
    inputlist = sys.stdin.read().splitlines()
    
    # print the smallest palindromic string that can be made for each input
    for i in inputlist:
        print( smallest_palindrome(i) )

if __name__ == "__main__":
    main()
