"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""

# Class Declaration
class Ceaser_Cipher_ciphertext:
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
#Take input of cipher text and key k
pt = input("Enter a Cipher Text:")
k = int(input("Enetr the Key:"))

#call the function with class
Ceaser_Cipher_ciphertext.plain_text(pt,k)