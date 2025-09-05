# program to take inputs in seconds and print output in the form of mins and seconds.

time_in_sec = int(input("enter time in secons: "))

min = time_in_sec // 60
secs = time_in_sec % 60

print("converted",time_in_sec,"to", min ,"mins", secs ,"seconds ")