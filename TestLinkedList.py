
#  File: TestLinkedList.py

#  Description: Create and Test LinkedList methods and class

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner UT EID: rtm2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/25

#  Date Last Modified: 10/26


class Link (object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # ------------------------------------------------------------------------------------
    # get number of links
    def get_num_links(self):
        current = self.first

        # Handles an Empty list
        if (self.is_empty()):
            return 0

        # While the next link isn't empty, increment numelements
        numelements = 1
        while (current.next != None):
            numelements += 1
            current = current.next

        return numelements
        
    # ------------------------------------------------------------------------------------
    # add an item at the beginning of the list
    def insert_first(self, data):
        # Handles empty list
        if (self.is_empty()):
            self.first = Link(data)
            return 
        
        # Creates new link that points to current head 
        # and points list head to newlink
        newLink = Link(data, self.first)
        self.first = newLink

    # ------------------------------------------------------------------------------------
    # add an item at the end of a list
    def insert_last(self, data):
        # Handles empty list
        if (self.is_empty()):
            self.first = Link(data)
            return

        # Sets current equal to last link
        current = self.first
        while (current.next != None):
            current = current.next

        # curent Last link is pointed to newLink
        # newLink is pointed to none
        newLink = Link(data)
        current.next = newLink

    # ------------------------------------------------------------------------------------
    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        # Handles empty list
        if (self.is_empty()):
            self.insert_first(data)
            return
        
        # Handles first element being greater than data
        if (data <= self.first.data):
            self.insert_first(data)
            return
        
        # initializes 2 variables to keep track of previous and current link
        # because this is a singly linked-list
        current = self.first
        previouslink = self.first

        # finds link with greater or equal data value
        while (data > current.data):
            # if end of list is reached, append newLink to end of list
            if (current.next == None):
                self.insert_last(data)
                return
            else:
                # increment through list
                previouslink = current
                current = current.next
        
        # sets newLink pointers and updates current pointers
        newLink = Link(data)
        previouslink.next = newLink
        newLink.next = current

    # ------------------------------------------------------------------------------------
    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        # check if list is empty
        if (self.is_empty()):
            return None

        while (current.data != data):
            # if you reached the end and it's not the data
            if (current.next == None):
                return None
            else:
                # else go to the next link
                current = current.next

        return current.data


    # ------------------------------------------------------------------------------------
    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        # check if list is empty
        if (current == None):
            return None

        while (current.data != data):
            # if you reached the end and it's not the data
            if (current.next == None):
                return None
            else:
                # if next linkdata is greater, the link wasn't here
                # makes this method faster for a sorted lsit
                if (data < current.next.data):
                    return None
                # else go to the next link
                current = current.next

        return current.data

    
    # ------------------------------------------------------------------------------------
    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        # initialize 2 variables to keep track of links because it is a 
        # singly linked list
        previous = self.first
        current = self.first

        #check for empty list
        if (current == None):
            return None

        # this block traverses link till datalink is found
        while (current.data != data):
            # if end is reached, link doesn't contain datalink
            if (current.next == None):
                return None
            else:
                # traverse linked-list
                previous = current
                current = current.next

        # handles first link being datalink
        if (current == self.first):
            self.first = current.next
        else:
            # This line does the actual link 'deletion'
            previous.next = current.next

        return current.data

     # ------------------------------------------------------------------------------------
        # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        # Handles empty list
        if (self.is_empty()):
            return 'Empty List'
        # Initialize currentnode pointer / string
        current = self.first
        finalstr = ''
        inc = 0

        while (current != None):    # goes through entire linked list
            # add currnode data to string
            finalstr = finalstr + str(current.data) + '  '
            inc += 1 #increment counter
            current = current.next #increment currentnode
            
            if (inc % 10 == 0): #every 10 items add new lines
                finalstr += '\n'

        return finalstr


     # ------------------------------------------------------------------------------------
        # Copy the contents of a list and return new list
        # do not change the original list
    def copy_list(self):
        # initialize LinkedList to be returned and currnode pointer
        newList = LinkedList()
        current = self.first
        
        while (current != None): # go through linkedlist
            newList.insert_last(current.data) # insert each node in new linkedlist
            current = current.next  #increment currnode

        return newList

        # Reverse the contents of a list and return new list
        # do not change the original list
    def reverse_list(self):
        # initialize LinkedList to be returned and currnode pointer
        newList = LinkedList()
        current = self.first
        
        # go through linked list nodes
        while (current != None):
            # insert each node at front to effectively reverse order
            newList.insert_first(current.data)
            current = current.next

        return newList

        # Sort the contents of a list in ascending order and return new list
        # do not change the original list
    def sort_list(self):
        # initialize LinkedList to be returned and currnode pointer
        newList = LinkedList()
        current = self.first
        
        # go through each node
        while (current != None):
            # insert_in_order does the sorting during insertion
            newList.insert_in_order(current.data)
            current = current.next

        return newList

        # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        if (self.first == None): # handle empty list
            return True
        
        current = self.first

        while (current.next != None):   # go through linked list
            # check each node is sorted compared to its next pointer
            if current.next.data < current.data: 
                return False
            else:
                current = current.next

        return True

        # Return True if a list is empty or False otherwise
    def is_empty(self):
        # If head points to None, list is empty
        if (self.first == None):
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        newList = LinkedList()
        current = self.first
        other_current = other.first
        
        while (current != None): # go through linked list
            newList.insert_last(current.data) # copy list to newlist
            current = current.next
        
        while (other_current != None): # go through linked list
            # add node in sorted order during insertion to newlist
            newList.insert_in_order(other_current.data) 
            other_current = other_current.next

        return newList

     # ------------------------------------------------------------------------------------
    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        # an empty list is not equal to a filled list
        if (self.is_empty() != other.is_empty()):
            return False
        # if different number of nodes, they're not equal by def.
        if (self.get_num_links() != other.get_num_links()):
            return False

        selfcurr = self.first
        othercurr = other.first

        while (selfcurr != None): # go through linked list
            if (selfcurr.data != othercurr.data): #compare nodes
                return False
            else:
                selfcurr = selfcurr.next    #increment currentnode.self
                othercurr = othercurr.next  #increment currentnode.other

        return True

     # ------------------------------------------------------------------------------------
    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        newList = LinkedList() #initialize linked list
        current = self.first   #initialize currnode pointer
        tracker = [] # list that keeps track of duplicate items
        while (current != None):    # go through lsit
            if (int(current.data) in tracker): # remove duplicate node
                current = current.next
            else:
                tracker.append(int(current.data)) # add new value to tracker
                newList.insert_last(current.data) # add non-duplicate to newlist
                current = current.next

        return newList

def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    tester = LinkedList()
    tester.insert_last(1)
    tester.insert_last(2)
    tester.insert_last(3)
    tester.insert_last(4)
    tester.insert_last(5)
    tester.insert_last(6)
    tester.insert_last(7)
    tester.insert_last(8)
    tester.insert_last(9)
    tester.insert_last(10)
    tester.insert_last(11)

    print(tester)
    # Test method insert_last()
    tester.insert_last(12)
    # Test method insert_in_order()



if __name__ == "__main__":
    main()