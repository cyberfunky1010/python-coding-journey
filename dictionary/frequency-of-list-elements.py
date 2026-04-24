import json

sentence = input("enter sentence: ")

words = sentence.split()

d = {}

for one in words:
    key = one
    if key not in d:    # this ensures program counts unique words only once. improves efficiency. 
        count = words.count(key)
        d[key] = count

print("counting frequencys in list: ", words)        
print(json.dumps(d, indent=2))        