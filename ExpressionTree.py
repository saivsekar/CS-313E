#  File: ExpressionTree.py

#  Description: Create Expression Tree and generate post,pre,and infix expressiosn

#  Student's Name: Sai Chandrasekar

#  Student's UT EID: svc439

#  Partner's Name: Reece Mathew

#  Partner's UT EID: rtm 2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/4

#  Date Last Modified: 11/7

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node (object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree (object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        # create a root node for expression tree
        self.root = Node(None)
        # create node stack
        exprStack = Stack()
        # creates node tracker
        currNode = self.root
        # lists are easier to deal with
        expr = expr.split() 

        for token in expr:
            
            # If the current token is a left parenthesis, add a new node as the left child of the current node. 
            # Push current node on the stack and make current node equal to the left child.
            if (token == '('):
                currNode.lChild = Node(token)   # add new node as left child of currNode
                exprStack.push (currNode)       # push currNOde onto stack
                currNode = currNode.lChild      # make currNode currNode's left child

            # If the current token is an operator, set the current node's data value to the operator. 
            # Push current node on the stack. Add a new node as the right child of the current node and make the current node equal to the right child.
            elif (token in operators):
                currNode.data = token           # set currNode data to operator token
                exprStack.push (currNode)       # push currNode on the stack
                currNode.rChild = Node(None)    # add new Node as currNode's right child
                currNode = currNode.rChild      # make currNode currNode's right child
            
            # If the current token is a right parenthesis, make the current node equal to the parent node by popping the stack if it is not empty.
            elif (token == ')'):
                if (not exprStack.is_empty() ): # make currNode equal to parent if stack is not empty
                    currNode = exprStack.pop()

            # If the current token is an operand, set the current node's data value to the operand and make the current node equal to the parent 
            # by popping the stack.
            else:
                # saves whole numbers as integers, and decimal numbers as floats
                number = float(token)
                if (number % 1 == 0):
                    currNode.data = int(token)
                elif (number % 1 != 0):
                    currNode.data = float(token)

                currNode = exprStack.pop()      # currNode is set to it's current parent by pooping the stack

            

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        # Recursive: keep evaluating results of left and right child till leaf node reached
        # to perform depth-first traversal
        if (aNode.data in operators):
            return self.eval ( self.evaluate(aNode.lChild), self.evaluate (aNode.rChild), aNode.data)
        
        # Base Case : leaf node is reached and operand is returned 
        else:
            return float(aNode.data)


    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        # Base Case: returns empty string upon null
        if (aNode == None):
            return ""
        
        # Recursive: returns parent (operator) , leftmost child, then backtracks up to rightchild 
        if (aNode != None):
            return str(aNode.data) + " " + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
            
        

    # this function recursively generates the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        # Base Case: returns empty string upon null
        if (aNode == None):
            return ""

        # Recursive: returns leftmost child, backtracks up the right children, then returns the parent node (operator)
        if (aNode != None):
            return self.post_order (aNode.lChild) + self.post_order (aNode.rChild) + str (aNode.data) + " "


    # helper function to carry out arithmetic operations. Self-explanatory
    def eval(self, op1, op2, operator):
        if (operator == '+'):
            return op1 + op2
             
        elif (operator == '-'):
            return op1 - op2

        elif (operator == '*'):
            return op1 * op2
        
        elif (operator == '/'):
            return op1 / op2
        
        elif (operator == '//'):
            return op1 // op2
        
        elif (operator == '%'):
            return op1 % op2

        elif (operator == '**'):
            return op1 ** op2
    

# you should NOT need to touch main, everything should be handled for you

def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print('Prefix Expression:', end=' ')
    print(tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print('Postfix Expression:', end=' ')
    print(tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
