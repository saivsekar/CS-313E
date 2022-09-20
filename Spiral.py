import sys
#  File: Spiral.py

#  Description: Creates a Prime Ulam number spiral with dimensions n*n (n being user input)

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 8/31/22

#  Date Last Modified: 9/2/22

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n


def populate(spiral):
  # Initializes dimension constant for spiral matrix (e.g. dimension = 11 for 11x11 matrix)
  DIMENSION = len(spiral)
  
  # Initializes the bounds of the 'box' part of the spiral populated
  low = 0
  high = DIMENSION - 1

  # Maxnum is the populator variable that fills the matrix elements. 
  # levels is the looped variable representing which 'box' the program is on
  maxnum = DIMENSION ** 2
  levels=int((DIMENSION + 1)/2)

  for level in range(0, levels):
    
      #loop fills in matrix right to left on top
      for i in range(low, high+1):
          spiral[level][DIMENSION-1-i]= maxnum
          # maxnum is incremented down 1 to represent each number in spiral matrix
          maxnum -= 1                  
          
      #loop fills matrix top left to bottom
      for i in range(low+1,high+1):
          spiral[i][low]= maxnum
          maxnum -= 1
    
      #loop fills matrix from bottom left to right
      for i in range(low+1,high+1):
          spiral[high][i]= maxnum
          maxnum -= 1

      #loop fills in matrix from bottom right back to top
      for i in range(high-1,low,-1):
          spiral[i][high]= maxnum
          maxnum -= 1
    
      # low and high change to match the dimensions of the 'box level' the program is at
      low += 1
      high -= 1

  return spiral




def create_spiral(n):
  
  if( n%2 == 0):
      n+= 1

  # Initializes 2D list of zeroes 
  spiral = []
  for i in range(n):
      newrow = []

      for j in range(n):
          newrow.append(0)

      spiral.append(newrow)

  finspiral = populate(spiral)

  return finspiral


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
  
  # initializes dimension constant and checker variable for exceptions
  DIMENSION = len(spiral)
  n_in_spiral = False


  # Utilizes nested for loops to run through spiral matrix and return index coords of number/determine checker
  for i in range(0, len(spiral)):
      if n in spiral[i]:
          n_in_spiral = True
          fin = spiral[i].index(n)
          x = i
          y = fin
          break
  
  # returns 0 if n DNE in spiral
  if not n_in_spiral:
    return 0

  #Initializes sum variable
  sum = 0

  # high is Highest possible index based on dimension of Spiral (e.g. 11x11 spiral, high = 10 )
  high = DIMENSION-1  

  # First block of code checks and returns sum if n is located in a corner 
  if x == 0 and y == 0:
      sum = spiral[x+1][x+1] + spiral[x+1][y] + spiral[x][y+1]
  elif x == 0 and y == high:
      sum = spiral[x][y-1] + spiral[x+1][y-1] + spiral[x+1][y]
  elif x == high and y == 0:
      sum = spiral[x-1][y] + spiral[x-1][y+1] + spiral[x][y+1]
  elif x == high and y == high:
      sum = spiral[x][y-1] + spiral[x-1][y] + spiral[x-1][y-1]
  else:
    # Second block of code checks and returns sum if n is located in edge row/cols of matrix
    if x == 0:
        sum = spiral[x][y-1] + spiral[x][y+1] + spiral[x+1][y-1] + spiral[x+1][y] + spiral[x+1][y+1]
    elif y == 0:
        sum = spiral[x-1][y] + spiral[x+1][y] + spiral[x-1][y+1] + spiral[x][y+1] + spiral[x+1][y+1]
    elif x == high:
        sum = spiral[x][y-1] + spiral[x][y+1] + spiral[x-1][y-1] + spiral[x-1][y] + spiral[x-1][y+1]
    elif y == high:
        sum = spiral[x-1][y] + spiral[x+1][y] + spiral[x-1][y-1] + spiral[x][y-1] + spiral[x+1][y-1]
    else:
        # This line returns sum of all adjacent values if located inside the matrix instead of the edges
        sum = spiral[x-1][y-1] + spiral[x][y-1] + spiral[x+1][y-1] + spiral[x-1][y] + spiral[x+1][y] + spiral[x-1][y+1] + spiral[x][y+1] + spiral[x+1][y+1]

  
  return sum

  

def main():
# read the input file
  dimension = int(sys.stdin.readline())
# create the spiral
  spiral = create_spiral(dimension)

# prints spiral in square format. Commented out bc not needed
#  for i in spiral:
#      print(i)

# processes the read-in text
  nlist = []
  for line in sys.stdin.readlines():
    line = int(line.strip())
    nlist.append(line)


# adds the adjacent numbers and prints the result
  for n in nlist:
    thesum = sum_adjacent_numbers(spiral, n)
    print(thesum)

if __name__ == "__main__":
  main()