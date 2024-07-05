"""

Name: Dhaval V Patel
Class: M.Sc. Cyber security
Sem: 2
Enrollment Number: 032200300002034
Practical lab: 3
Aim: Program1: Write a program to demonstrate Caeser Cipher Cryptosystem.

"""

def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  # print(key)
  return("" . join(key)) 
  
def encryption(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text))

if __name__ == "__main__": 
  string = input("Enter the message: ").upper()
  string = string.replace(" ","")
  keyword = input("Enter the keyword: ").upper()
  key = generateKey(string, keyword) 
  encrypt_text = encryption(string,key) 
  print("Encrypted message:", encrypt_text)