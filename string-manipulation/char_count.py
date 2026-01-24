#program that reads a line and prints number of digits, uppercase, lowercase and alphabets

char = input("enter strings of character:")

uppercase = lowercase = 0
digitcount = alphacount = 0

for a in char:                        # alternative way
    if a.isalpha():                   # if a.islower():
        alphacount+=1                 #       lowercase+=1
        if a.islower():               #       alphacount+=1
            lowercase+=1              # elif a.isupper():
        else:                         #       uppercase+=1
            uppercase+=1              #       alpharcount+=1
                                      #
    elif a.isdigit():                 # elif a.digit()
        digitcount+=1                 #       digitcount+=1

print('number of lowercases: ',lowercase)                    
print('number of uppercase: ',uppercase)                    
print('number of alphacount: ',alphacount)                    
print('number of digits: ',digitcount)                    