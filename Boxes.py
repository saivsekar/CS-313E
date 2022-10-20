
#  File: Boxes.py

#  Description: Given a  list of boxes with 3 dimensions, find the 
#               largest number of nested box sets and the number of
#               these largest sets

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/15

#  Date Last Modified: 10/18

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes

def nesting_boxes(box_list):
    # initialize memo and subset list
    memo = []
    b = []
    # uses brute force to get list of every possible subset
    sub_sets(box_list, b, 0, memo)

    # extracts every subset of nested boxes from total list
    finallist = []
    for i in memo:
        if (listfits(i)):
            finallist.append(i)

    max = 0
    # gets maximum number of boxes that fit inside each other using len(i) 
    # as # of boxes variable
    for i in finallist:
        if len(i) > max:
            max = len(i)

    # gets number of ^^ sets of nesting boxes
    count = 0
    for i in finallist:
        if len(i) == max:
            count += 1

    return max, count


# checks that a given list of boxes are nested
def listfits(boxlist):
    check = True

    # checks each successive box fits outside previous box
    for i in range(len(boxlist)-1):
        check = check and (does_fit(boxlist[i], boxlist[i+1]))
    return check

# Gets all subsets of boxes


def sub_sets(boxes, b, idx, memo):
    # boxes is the list of every box
    # b is the subset of boxes we're looking at
    # memo is the memoization tool
    # shoutout to Professor Mitra for lecture subsets.py

    hi = len(boxes)
    if (idx == hi):
        memo.append(b)
        return
    else:
        c = b[:]
        b.append(boxes[idx])

        # added to prevent time exception
        # checks that the b subset is actually nested so we don't waste memory 
        if( listfits(b) ):
            sub_sets(boxes, b, idx+1, memo)
        
        # added to prevent time exception
        # checks that the c subset is actually nested so we don't waste memory
        if( listfits(c) ):
            sub_sets(boxes, c, idx + 1, memo)


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])

        box.sort()
        box_list.append(box)

    # print to make sure that the input was read in correctly
    #print(box_list)
    #print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    #print(box_list)
    #print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(box_list)

    # print the largest number of boxes that fit
    print(max_boxes)

    # print the number of sets of such boxes
    print(num_sets)


if __name__ == "__main__":
    main()
