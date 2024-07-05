"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""

# Class Declaration
class Ceaser_Cipher:
    def cipher_text(pt,k):
        #Take input of plain text and key k
        pt = pt.upper()
        ci_text = ""
        
        #remove space from the string
        pt = pt.replace(" ","")
        
        #Give one by one input of a string caracter
        for i in range(len(pt)):
            #check if the character is in upper case or lower case
            if (pt[i].isupper()) :
                #conver character in ascii and then do a conversion so that we can perfor encryption
                #cipher text = (plain text + key) mod 26
                #here we take the value of A as a 0 that's why we subtrac 65 from any character ascii value and add key to perfrom mod 26
                #them again add 65 so the acii value is matched
                ci_text += chr((((ord(pt[i]))-65)+k)%26 + 65)
        #print a encrypted value
        print(ci_text)

#Take input from the user
pt = input("Enter a Plain Text:")
k = int(input("Enetr the Key:"))

#call the function With class
Ceaser_Cipher.cipher_text(pt,k)