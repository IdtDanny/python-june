import pandas as pd

data = {'Employee_ID' : ['2401', '2402'],
        'Name' : ['Danny', 'David'],
        'Department' : ['Management', 'Engineer'],
        'Date': ['15 June', '01 July'],
        'Status': ['Present', 'Absent']}

attendance = pd.read_csv('Attendance.csv')

# attendance = pd.DataFrame(data)

print(attendance)