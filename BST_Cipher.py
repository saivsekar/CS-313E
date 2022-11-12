#  File: BST_Cipher.py

#  Description: Create BST key to encrypt/decrpyt message

#  Student's Name: Sai Chandrasekar

#  Student's UT EID: svc439

#  Partner's Name: Reece Mathew

#  Partner's UT EID: rtm 2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/8

#  Date Last Modified: 11/9

import sys


class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        # Never really used 
        return str(self.data)

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None

        # convert all chars to lowercase
        encrypt_str = encrypt_str.lower()
        # go through string, making key tree from each valid char
        for token in encrypt_str:
            # for every lowercase letter in the alphabet and a space
            if ((96 < ord(token) < 123) or (ord(token) == 32)):
                self.insert(token)


    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new_node = Node(ch)

        # Insert into Empty Tree
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root

            # Find spot to insert new Node based on BST rules
            while (current != None):

                # Prevent duplicate chars in tree
                if (current.data == ch):
                    return

                parent = current
                if (ch < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # Insert node based on BST rules
            if (ch < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node




    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        code = ''
        # Handle empty tree
        if (self.root == None):
            return code
        # Handle ch being root
        if (self.root.data == ch):
            return '*'

        current = self.root
        while (current != None) and (current.data != ch):
            if (ch < current.data):
                code += '<'
                current = current.lchild
            else:
                code += '>'
                current = current.rchild

        if (current == None):
            return ''
            
        return code

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        if (self.root == None):
            return ''
        
        # create node tracker
        current = self.root  
        # Go through coded string
        for token in st:
            # '*' indicates root is the char we want
            if (token == '*'):
                return self.root.data
            elif (token == '>'):
                current = current.rchild
            elif (token == '<'):
                current = current.lchild
            
            # Null node indicates invalid character
            if (current == None):
                return ''
        
        return current.data
                
            

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        # if tree is empty, there's no way to encrypt
        if (self.root == None):
            return
        
        # create list to store encoded message
        # created as list to make '!'.join() work
        codemsg = []
        # convert all chars to lowercase
        st = st.lower()
        # go through string, encrypting each valid char
        for token in st:
            # for every lowercase letter in the alphabet and a space
            if ( (96 < ord(token) < 123) or (ord(token) == 32) ):
                codemsg.append(self.search(token))
        
        # Insert delimeter '!' character
        codemsg = '!'.join(codemsg)

        return codemsg

        

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        # Can't decrypt without a key
        if (self.root == None):
            return
        
        # create list to hold decoded string
        # created as list to make '!'.join() work
        decoded = ''
        # gets rid of delimiter
        st = st.split('!')
        for codetoken in st:
            decoded += (self.traverse(codetoken))
        
        return decoded
    
    
def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()
