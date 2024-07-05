"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""

# Class Declaration
class Ceaser_Cipher_plaintext:
    
    def plain_text():
    
        #Take input of cipher text and key k
        ct = input("Enter a Cipher Text:")
        k = int(input("Enetr the Key:"))
        
        plain_text = ""
        
        #Give one by one input of a string character
        for i in range(len(ct)):
            plain_text+= chr(((ord(ct[i]))-k)%126)
        
        #print a encrypted value
        print(plain_text)

    #call the function ith class
Ceaser_Cipher_plaintext.plain_text()