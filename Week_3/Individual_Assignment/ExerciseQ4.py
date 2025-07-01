"""
Write a Python program that collects the marks of a student in five modules:
Python, ICT, Cryptography, Operations Research and Linear Algebra. The program should:
a.	Prompt the user to enter a mark for each of the five modules.
b.	Calculate and display:
i.	The average mark
ii.	The highest mark among the five
iii.	The overall grade, based on the average, using the grading scale below:
Average Score	Grade
80 – 100	A (Excellent)
70 – 79	B (Very Good)
60 – 69	C (Good)
50 – 59	D (Pass)
Below 50	F (Fail)
3.	Validate that all marks entered are numeric and fall between 0 and 100.
"""
module={'Python':0.0,'ICT':0.0,'Cryptography':0.0,'Operations Research':0.0,'Linear Algebra':0.0}
total=0
maximum=module['Python']
max_module=module['Python']
for key,values in module.items():
    module[key]=float(input(f'{key}: '))
    total+=module[key]
    if maximum<module[key]:
        maximum=module[key]
        max_module=key
average=total/len(module)
print(f'The average mark is:{average}%')
if average<100:
    if average>80:
        print('A (Excellent)')
    elif 70<= average<80:
        print('B (Very Good)')
    elif 60<= average<70:
        print('C (Good)')
    elif 50<= average<60:
        print('D (Pass)')
    else:
        print('F (Fail)')
else:
    print('out of range')

print(f'The highest mark is:{maximum:.0f}% for {max_module}')
