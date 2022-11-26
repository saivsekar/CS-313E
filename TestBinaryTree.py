#  File: TestBinaryTree.py

#  Description: Create and test methods for Binary Tree

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner's UT EID: rtm 2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/9

#  Date Last Modified: 11/9

import sys


class Node (object):
    def __init__(self, data = None):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        # Never really used
        return str(self.data)



class Tree (object):
    # the init() function creates the binary search tree with the
    # given data
    def __init__(self, data = None):
        self.root = None
        self.data = data
        # go through data list, inserting into tree
        if( data != None):
            for token in data:
                self.insert(token)


    def insert(self, data):
        new_node = Node(data)

        # Insert into Empty Tree
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root

            # Find spot to insert new Node based on BST rules
            while (current != None):

                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # Insert node based on BST rules
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    def search (self, data):
        current = self.root

        while (current != None) and (current.data != data):
            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild

        return current

    #---------------------------------------------------------------------------------------------------------------
    def is_similar (self, pNode):
        return self.similar_helper (self.root, pNode.root)
    
    def similar_helper(self, selfNode, otherNode):
        # Base Case if both trees reach null together
        if (selfNode == None and otherNode == None):
            return True

        # Goes through each tree, recursively comparing them
        elif (selfNode != None and otherNode != None):
            return (selfNode.data == otherNode.data) and self.similar_helper(selfNode.lchild, otherNode.lchild)\
                and self.similar_helper (selfNode.rchild, otherNode.rchild)
        
        # if selfNode is null while otherNode is not, the trees by definition cannot be similar
        return False
        
            
    #---------------------------------------------------------------------------------------------------------------
    def get_level (self, level):
        return []
    
    #---------------------------------------------------------------------------------------------------------------
    def get_height (self):
        return self.height_helper(self.root)

    def height_helper(self, node):
        # Base Case: Null node does not have a level
        if (node == None):
            return 0
        
        # Recursive: Go down each possible route and get max number of level
        # max() function does comparison for us. 1 is added to address root node level
        else:
            return max (self.height_helper(node.lchild), self.height_helper(node.rchild)) + 1

    #---------------------------------------------------------------------------------------------------------------
    def num_nodes (self):
        # Recursively get total nodes, starting at root node for full tree
        numnodes = self.numnode_helper (self.root)
        return numnodes

    def numnode_helper (self, aNode):
        # base case: aNode is a null pointer
        if (aNode == None):
            return 0
        else:
            # returns 1 (for the current Node) plus number of nodes in each recursive left and right subtree
            return 1 + self.numnode_helper (aNode.lchild) + self.numnode_helper (aNode.rchild)
    #---------------------------------------------------------------------------------------------------------------


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints

    # Make three trees
    tree1 = Tree (tree1_input)
    tree2 = Tree (tree2_input)
    tree3 = Tree (tree3_input)

    # Test your method is_similar()
    if (tree1.is_similar(tree2)):
        print ("Tree 1 is similar to Tree 2")
    
    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different
    print(f'The height of tree 1 is {tree1.get_height()}')
    print(f'The height of tree 2 is {tree2.get_height()}')
    print(f'The height of tree 3 is {tree3.get_height()}')
    # Get the total number of nodes a binary search tree
    print(f'Total nodes in tree 1 is {tree1.num_nodes()}')
    print(f'Total nodes in tree 2 is {tree2.num_nodes()}')
    print(f'Total nodes in tree 3 is {tree3.num_nodes()}')

if __name__ == "__main__":
  main()
