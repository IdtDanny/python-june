from itertools import count

import pandas as pd

data = {'Employee_ID' : ['2401', '2402'],
        'Name' : ['Danny', 'David'],
        'Department' : ['Management', 'Engineer'],
        'Date': ['15 June', '01 July'],
        'Status': ['Present', 'Absent']}

df = pd.read_csv('Attendance.csv')

# attendance = pd.DataFrame(data)

# print(df)

# Total Present is the Sheet

print(df.columns)

count = (df['Day 1'] == 1).sum

df.groupby('Contact').count()

print(count)