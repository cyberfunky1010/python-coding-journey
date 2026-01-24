# program that reads a line and a substring and tells occurences of substring in the line.

line = input("enter a line: ")
sub = input("enter substring: ")

sublen = len(sub)
start = count = 0

while True:
    pos = line.find(sub,start)
    if pos != -1:                       #pos + 1 - move 1 step forward, even if character overlaps
        count+=1                        #pos + sublen - skip the entire matched substring
        start = pos + sublen #no overlapping. this makes sure index is moving sub-string by sub-string and not by 1 (pos + 1) - this counts overlapping characters
    else:
        break

print("number of occurencees of",sub,count)        

# when to use which: 
# pos + 1 - you want all possible matches. overlapping allowed. pattern detection.
# pos + sublen - want distinct occurences. text processing/exams/ word counting.