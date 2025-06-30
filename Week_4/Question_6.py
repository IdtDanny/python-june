import pandas as pd

data = {'Employee_ID': ['2401', '2402'],
        'Name': ['2401', '2402'],
        'Department': ['2401', '2402'],
        'Date': ['2401', '2402'],
        'Status': ['Present', 'Absent']
        }

attendance = pd.DataFrame(data)

print(attendance)