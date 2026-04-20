# basic program illustrating nested dictionary.

employee = { 'john' : { 'age' : 25, 'salary': 70000}, 'sam': { 'age' : 24, 'salary' : 90000}}

for key in employee:
     
     print()
     print('employee', key, ':')
     print('age:',(employee[key]['age']))
     print('salary',employee[key]['salary'])