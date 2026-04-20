# program that takes marks input and print marks of student like: ( (45,57,68), (68, 68, 88), (66, 58, 78), ......)

all_stu_rec = ()  # initialize emply tuple to store students records. 

for i in range(1,6):
    
    print("student :",i)
    sub1 = int(input("enter marks of subject 1: "))
    sub2 = int(input("enter marks of subject 2: "))
    sub3 = int(input("enter marks of subject 3: "))

    student_marks = (sub1,sub2,sub3)  # inner tuple of student marks 

    all_stu_rec += (student_marks,)   # append inner tuple to all student records.
    print()

print("marks of all students: ")    
print(all_stu_rec)    