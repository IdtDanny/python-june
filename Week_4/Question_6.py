import pandas as pd

data = {'Employee_ID': ['2401', '2402', '2403', '2404', '2405'],
        'Name': [],
        'Department': [],
        'Date': [],
        'Status': ['Present', 'Absent']
        }

attendance = pd.read_csv(data)