"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""

# Class Declaration
class Ceaser_Cipher_with_all:
    
    def cipher_text():
    
        #Take input of plain text and key k
        pt = input("Enter a Plain Text:")
        k = int(input("Enetr the Key:"))
        
        ci_text = ""
        
        #Give one by one input of a string caracter
        for i in range(len(pt)):
            ci_text += chr(((ord(pt[i]))+k)%126)
        
        #print a encrypted value
        print(ci_text)

#call the function ith class
Ceaser_Cipher_with_all.cipher_text()