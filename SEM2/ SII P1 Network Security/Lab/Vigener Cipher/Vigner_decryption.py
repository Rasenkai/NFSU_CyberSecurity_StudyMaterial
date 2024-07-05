"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""
def generateKey(cipher_text, key): 
  key = list(key) 
  if len(cipher_text) == len(key): 
    return(key) 
  else: 
    for i in range(len(cipher_text) -len(key)): 
      key.append(key[i % len(key)]) 
#   print(key)
  return("" . join(key)) 
   
def decryption(cipher_text, key): 
  orig_text = [] 
  for i in range(len(cipher_text)): 
    x = (ord(cipher_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

# if __name__ == "__main__": 
cipher_text = input("Enter the message: ").upper()
cipher_text = cipher_text.replace(" ","")
keyword = input("Enter the keyword: ").upper()
key = generateKey(cipher_text, keyword)  
print("Decrypted message:", decryption(cipher_text, key))
