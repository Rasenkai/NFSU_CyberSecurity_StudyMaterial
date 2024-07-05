
"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""
# Class Declaration
class Ceaser_Cipher_encryption:
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

class Ceaser_Cipher_decryption:
    def plain_text(ct,k):

        ct = ct.upper()
        plain_text = ""
        
        #remove space from the string
        ct = ct.replace(" ","")
        
        #Give one by one input of a string caracter
        for i in range(len(ct)):
            if (ct[i].isupper()) :
                #conver character in ascii and then do a conversion so that we can perfor decryption
                #Plain text = (Cipher text - key) mod 26
                #here we take the value of A as a 0 that's why we subtrac 65 from any character ascii value and add key to perfrom mod 26
                #them again add 65 so the acii value is matched
                plain_text+= chr((((ord(ct[i]))-65)-k)%26 + 65)
       
        #print a Plain Text
        print(plain_text)

#Take input from the user
Text = input("Enter a Text:")
k = int(input("Enetr the Key:"))

print("What you want to do:")
print("1. Encryption")
print("2. Decryption")

u_choise = int(input("Choise 1 or 2:"))

if u_choise==1:
    #call the function With class
    Ceaser_Cipher_encryption.cipher_text(Text,k)

if u_choise==2:
    #call decryption class function
    Ceaser_Cipher_decryption.plain_text(Text,k)