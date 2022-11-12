#  File: Poly.py

#  Description: Display and perform basic operations on input polynomial expressions

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/2

#  Date Last Modified: 11/4

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

# returns True is polynomial expression link_a is greater than other, link_b
# returns False if not
def is_greater_equal(link_a, link_b):
        # compare exponent values
        if link_a.exp > link_b.exp:
            return True
        elif link_a.exp < link_b.exp:
            return False
        else:
            # compare base coefficient if exponents are the same
            return ( link_a.coeff >= link_b.coeff )

# add links
def add_links(link_a, link_b):
    # assuming similar coefficients, return singular Link with
    # sum of previous exponents as new exponent
    a_coeff = link_a.coeff
    b_coeff = link_b.coeff
    exp = link_a.exp

    return Link(a_coeff + b_coeff, exp)

# multiply links
def multiply_links(link_a, link_b):
    a_coeff = link_a.coeff
    b_coeff = link_b.coeff
    a_exp = link_a.exp
    b_exp = link_b.exp

    return Link(a_coeff * b_coeff, a_exp + b_exp)

def add_like_exponents(self):
    # initialize linkedList for polynomial
    newPoly = LinkedList()
    # initialize link tracker at head
    new_current = self.first
    while (new_current != None): #iterates through linkedList
        # initializes variables keeping track of important values
        checker_current = new_current
        coeff = 0
        exp = new_current.exp
        counter = 0
        # adds similar exponent terms together, creating a new link
        while (checker_current != None) and (exp == checker_current.exp):
            coeff += checker_current.coeff
            checker_current = checker_current.next
            counter += 1
        if (coeff != 0): # inserts new link with added exponents
            newPoly.insert_last(coeff, exp)
        
        for i in range(counter-1):
            if new_current == None: # check for end of list
                break
            new_current = new_current.next
            
        if new_current != None: # increment link tracker
            new_current = new_current.next

    return newPoly

class LinkedList (object):
    def __init__ (self):
        self.first = None
    
    # add an item at the beginning of the list
    def insert_first(self, coeff, exp):
        # Handles empty list
        if (self.first == None):
            self.first = Link(coeff, exp)
            return 
        
        # Creates new link that points to current head 
        # and points list head to newlink
        newLink = Link(coeff, exp, self.first)
        self.first = newLink
    
    # add an item at the end of a list
    def insert_last(self, coeff, exp):
        # Handles empty list
        if (self.first == None):
            self.first = Link(coeff, exp)
            return 

        # Sets current equal to last link
        current = self.first
        while (current.next != None):
            current = current.next

        # curent Last link is pointed to newLink
        # newLink is pointed to none
        newLink = Link(coeff, exp)
        current.next = newLink

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        newLink = Link(coeff, exp)

        if (self.first == None):
            self.first = newLink
            return

        if is_greater_equal(newLink, self.first):
            self.insert_first(coeff, exp)
            return

        # initializes 2 variables to keep track of previous and current link
        # because this is a singly linked-list
        current = self.first
        previouslink = self.first

        # finds link with greater or equal data value
        while (is_greater_equal(current, newLink)):
            # if end of list is reached, append newLink to end of list
            if (current.next == None):
                self.insert_last(coeff, exp)
                return
            else:
                # increment through list
                previouslink = current
                current = current.next
        
        # sets newLink pointers and updates current pointers
        previouslink.next = newLink
        newLink.next = current


    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        newPoly = LinkedList()
        current = self.first
        p_current = p.first

        # add expressions of polynomials and insert to new LinkedList up until
        # one of the polynomials runs out of expressions
        while (current != None):
            newPoly.insert_in_order(current.coeff, current.exp)
            current = current.next

        while (p_current != None):
            newPoly.insert_in_order(p_current.coeff, p_current.exp)
            p_current = p_current.next

        # adds remaining expressions of polynomial that hasn't run out

        return add_like_exponents(newPoly)

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        newPoly1 = LinkedList() # create linkedList in which results are deposited
        current = self.first
        p_current = p.first

        while (current != None): # iterate through linkedList
            while (p_current != None): # go through populating results LinkedList
                newLink = multiply_links(current, p_current)  # multiplies Link elements
                newPoly1.insert_in_order(newLink.coeff, newLink.exp) # does sorting for us
                p_current = p_current.next 
            current = current.next
            p_current = p.first

        return add_like_exponents(newPoly1) # simplify new LinkedList for like terms
                

    # create a string representation of the polynomial
    def __str__ (self):
        if (self.first == None):
            return None

        current = self.first
        finalstr = ''

        # adds polynomial expression and ' + '
        while (current != None):
            finalstr += f'({current.coeff}, {current.exp}) + '
            current = current.next
        
        # removes ' + ' at end of polynomial
        if (current == None) and (finalstr != ''):
            finalstr = finalstr[:len(finalstr) - 3]

        return finalstr



def main():
    # read data from file poly.in from stdin

    # create polynomial p
    p = LinkedList()

    line = sys.stdin.readline()
    line = line.strip()
    num_expr = int (line)

    for i in range(num_expr):
        p_num = sys.stdin.readline()
        p_num = p_num.strip()
        p_num = p_num.split()
        for j in range(len(p_num)):
            p_num[j] = int(p_num[j])

        p_coeff = p_num[0]
        p_exp = p_num[1]
        p.insert_last(p_coeff, p_exp)


    # create polynomial q
    q = LinkedList()

    space = sys.stdin.readline() # accounts for space between two polynomials
    line = sys.stdin.readline()
    line = line.strip()
    num_expr = int (line)

    for i in range(num_expr):
        q_num = sys.stdin.readline()
        q_num = q_num.strip()
        q_num = q_num.split()
        for j in range(len(q_num)):
            q_num[j] = int(q_num[j])

        q_coeff = q_num[0]
        q_exp = q_num[1]
        q.insert_last(q_coeff, q_exp)

    # get sum of p and q and print sum
    addition = p.add(q)
    print(addition)

    # get product of p and q and print product
    product = p.mult(q)
    print(product)

if __name__ == "__main__":
    main()