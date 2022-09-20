
#  File: DNA.py
# USE IN STATEMENT
#  Description:

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: 

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 8/24

#  Date Last Modified: 8/24

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

def longest_subsequence (s1, s2):
    commonseqs = []
    s1seqs = all_substrings(s1)
    s2seqs = all_substrings(s2)

    #gets all common substrings 
    for s in s1seqs:
      if (s in s2seqs):
        commonseqs.append(s)
    
    max = 0
    ix = 0
    
    #gets length of largest common subseqs
    for i in commonseqs:
      if (len(i) >= max):
        max = len(i)
    
    #gets longest subseqs
    longestseqs = []
    for i in commonseqs:
      if(len(i) == max):
        longestseqs.append(i)
  
    return sorted(list(set(longestseqs)))

#Code from lecture 8/29, thanks Dr. Mitra
def all_substrings(s):
    #define a list to store substrings
    result = []

    #define length of window
    wnd = len(s)

    #generate all substrings
    while (wnd > 0):
        idx = 0
        while((idx + wnd) <= (len(s))):
            sub_str = s[idx:idx+wnd]
            result.append(sub_str)
            idx += 1
        #decrease window size
        wnd -= 1

    return result   

    pass

def main():
  # read the number of pairs
  num_pairs = sys.stdin.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # for each pair call the longest_subsequence
  for i in range (num_pairs):
    st1 = sys.stdin.readline()
    st2 = sys.stdin.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper()
    st2 = st2.upper()

    # get the longest subsequences
    long_sub = longest_subsequence (st1, st2)

    # print the result
    if(len(long_sub) != 0):
     for i in long_sub:
       print(i)
    else:
      print("No Common Sequence Found")
      
    # insert blank line
    print()

if __name__ == "__main__":
  main()