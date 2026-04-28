import json

# Initialize an empty dictionary
student_data = {}

# Use a loop to add 10 students (simplified loop for example)
for i in range(1, 11):
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    grade = input("Enter Grade: ")
    
    # Storing details as a nested dictionary for better structure
    student_data[roll] = {"Name": name, "Marks": marks, "Grade": grade}

print(json.dumps(student_data, indent=2))
