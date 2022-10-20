
#  File: Triangle.py

#  Description:

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2234

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/7

#  Date Last Modified: 10/7

import sys


from timeit import timeit

# returns the greatest path sum using exhaustive search


def brute_force(grid):

    # helper function initialized inside wrapper function for direct interaction
    def bruteforce_helper(grid, sum, row, col, sumlist):
        # Adds current value to pathsum
        sum += grid[row][col]

        # Adds total pathsum of 1 path to sumlist
        if(row == len(grid) -1):
            sumlist.append(sum)
        
        else:
            # Pathsum continues directly downwards 1 row
            bruteforce_helper (grid, sum, row+1, col, sumlist)
            # Pathsum continues downwards 1 row and to the right 1 col
            bruteforce_helper (grid, sum, row+1 , col+1 , sumlist)

    # initialize list of pathsums
    sumlist = []

    # populate sumlist with all possible pathsums
    bruteforce_helper(grid, 0, 0, 0, sumlist)

    # sort and return largest pathsum
    sumlist = sorted(sumlist)
    return sumlist[-1]
    

# returns the greatest path sum using greedy approach

def greedy(grid):
    return
    

# returns the greatest path sum using divide and conquer (recursive) approach


def divide_conquer(grid):
    return

# returns the greatest path sum and the new grid using dynamic programming


def dynamic_prog(grid):
    return

# reads the file and returns a 2-D list that represents the triangle


def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

  # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    
    # check that the grid was read in properly
    # print (grid)
    
    #-----------------------------------------------------------------------------------------
    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(
        grid), 'from __main__ import brute_force', number=10)
    times = times / 10

    print(f'The greatest path sum through exhaustive search is \n{brute_force(grid)}')

    # print time taken using exhaustive search
    print(
        f'The time taken for exhaustive search in seconds is \n{times}')
    #-----------------------------------------------------------------------------------------


    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(
        grid), 'from __main__ import greedy', number=10)
    times = times / 10

    # print time taken using greedy approach


    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(
        grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10

    # print time taken using divide-and-conquer approach


    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(
        grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    
    # print time taken using dynamic programming


if __name__ == "__main__":
  main()
