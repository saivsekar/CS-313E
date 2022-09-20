#  File: Cipher.py

#  Description: Encrypts first line of input and decrypts second line of input

#  Student Name: Reece Mathew

#  Student UT EID: rtm2244

#  Partner Name: Sai Chandrasekar

#  Partner UT EID: svc439

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/10/2022

#  Date Last Modified: 9/10/2022

import sys
import math

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
    # total string length
    sq = len(strng)

    # initializes empty list to be filled in
    encrypt_list = []

    # adds string to be encrypted as a list
    for i in strng:
        encrypt_list.append(i)

    # returns the sqrt of the smallest square # greater than/equal to sq
    listdimen = math.ceil(math.sqrt(sq))

    # populates encryption 2d list with asterisk padding
    to_encrypt_spiral= [["*" for i in range(listdimen)] for j in range(listdimen)]

    # replaces appropriate elements with characters, leaving 'padding'
    for i in range(listdimen): 
        for j in range(listdimen):
            if len(encrypt_list) != 0:
                to_encrypt_spiral[i][j] = encrypt_list[0]
                encrypt_list.pop(0)

    # populates final 2d list with asterisk padding
    encrypted_spiral = [["*" for i in range(listdimen)] for j in range(listdimen)]

    # feeds in elements to rotated position value on final 2d list
    for i in range(listdimen): 
        for j in range(listdimen):
            encrypted_spiral[i][j] = to_encrypt_spiral[(listdimen-1)-j][i]

    #initializes final string
    encrypted_message = ""

    #populates string with characters that are not padding
    for i in range(listdimen): 
        for j in range(listdimen):
            if encrypted_spiral[i][j] != "*":
                encrypted_message += encrypted_spiral[i][j]

    return encrypted_message


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
    #total string length
    sq = len(strng)

    # initializes empty list to be filled in
    decrypt_list = []

    # adds string to-be-decrypted as a list
    for i in strng:
        decrypt_list.append(i)

    # returns the sqrt of the smallest square # greater than/equal to sq
    listdimen = math.ceil(math.sqrt(sq))

    # populates encryption 2d list with asterisk padding
    to_decrypt_spiral= [["*" for i in range(listdimen)] for j in range(listdimen)]

    # replaces appropriate elements with characters, leaving 'padding'
    for i in range(listdimen): 
        for j in range(listdimen):
            if len(decrypt_list) != 0:
                to_decrypt_spiral[i][j] = decrypt_list[0]
                decrypt_list.pop(0)

    # populates final 2d list with asterisk padding
    decrypted_spiral = [["*" for i in range(listdimen)] for j in range(listdimen)]

    # feeds in elements to rotated position value on final 2d list
    for i in range(listdimen): 
        for j in range(listdimen):
            decrypted_spiral[i][j] = to_decrypt_spiral[j][(listdimen-1)-i]

    # initializes final string
    decrypted_message = ""

    # populates final string with non-padding characters from 2d list
    for i in range(listdimen): 
        for j in range(listdimen):
            if decrypted_spiral[i][j] != "*":
                decrypted_message += decrypted_spiral[i][j]

    return decrypted_message

def main():
  # read the two strings P and Q from standard imput
    P = sys.stdin.readline().strip()
    Q = sys.stdin.readline().strip()
  # encrypt the string P
    encrypted_message = encrypt(P)
  # decrypt the string Q
    decrypted_message = decrypt(Q)
  # print the encrypted string of P and the 
  # decrypted string of Q to standard out
    print(encrypted_message)
    print(decrypted_message)

if __name__ == "__main__":
  main()