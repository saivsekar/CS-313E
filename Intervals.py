#  File: Intervals.py
# 
#  Description: Merge Intersecting Intervals

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/5

#  Date Last Modified: 9/9
#----------------------------------------------------------------------------
import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):

    #initialize empty list to hold merged intervals
    mergedlist = []
    # tuple list is sorted ascending by first value for speed
    tuples_list.sort()

    # initializes numhigh/numlow variables to act as endpoints for intervals
    numhigh = tuples_list[0][1]
    numlow = tuples_list[0][0]

    for idx in range(1, len(tuples_list)):
      
        # checks if current interval is in numlow-high interval
        if( tuples_list[idx][0] <= numhigh):

            # 'pass' if end of current interval is in numlow-interval
            if( tuples_list[idx][1] <= numhigh):
                pass
            else:
                # we have a new numhigh
                numhigh = tuples_list[idx][1]
          
        # appends merged interval to list and starts new numlow-high interval
        else:
            mergedlist.append((numlow,numhigh))
            numlow = tuples_list[idx][0]
            numhigh = tuples_list[idx][1]
    
    # appends final numlow-high interval to list as last merged interval
    mergedlist.append((numlow,numhigh))

    return mergedlist

    
    


# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):

  # tuples_list is first sorted numerically based on first value
  tuples_list.sort()
  # tuples_list is then sorted based on interval size 
  return sorted(tuples_list, key = lambda intvsz: (intvsz[1]-intvsz[0]))
  
    

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases
  assert merge_tuples([(21,28),(23,41)]) == [(21,41)]
  assert merge_tuples([(15,38),(37,42),(3,9)]) == [(3,9),(15,42)]


  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases
  assert sort_by_interval_size([(8,11),(16,17)]) == [(16,17),(8,11)]
  assert sort_by_interval_size([(12,100),(12,101)]) == [(12,100),(12,101)]

  return "all test cases passed"



def main():
  # open file intervals.in and read the data and create a list of tuples
  originaltuplelist = []

  # for loop processes each pair of read-in numbers as a tuple in a list
  numtuples = int(sys.stdin.readline())
  for i in range(numtuples):
      line = sys.stdin.readline()
      line = line.strip()
      line = line.split()
      originaltuplelist.append( (int(line[0]),int(line[1])) )


  # merge the list of tuples
  mergedlist = merge_tuples(originaltuplelist)

  # sort the list of tuples according to the size of the interval
  sortedmergedlist = sort_by_interval_size(mergedlist)
  
  # run your test cases
  #print (test_cases())

  # write the output list of tuples from the two functions
  print(mergedlist)
  print(sortedmergedlist)

if __name__ == "__main__":
  main()