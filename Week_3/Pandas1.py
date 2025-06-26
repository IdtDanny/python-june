import pandas as pd

Result = {'Names': ['Danny', 'Straton', 'Ange', 'Gloria'], 'Score': [90, 80, 90, 90], 'Session': ['Weekend', 'Evening', 'Evening', 'Evening']}

framedData = pd.DataFrame(Result)

print(framedData)

# View first few rows
print(f'\nThe very first few rows: \n{framedData.head()}')

# View first 2 rows
print(f'\nThe very first 2 rows: \n{framedData.head(2)}')

# View statistics
print(f'\nThe Table statistics: \n{framedData.describe()}')

# View the tabular information and types
print(f'\n\nThe Information Summary: \n{framedData.info()}')

# Get column and rows
print(f'\nThe (rows, columns) : \n{framedData.shape}')

# Get columns details
print(f'\nThe Columns information: \n{framedData.columns}')

# Min value and max value
print(f'\nThe Minimum Score: {min(framedData.Score)} \nThe Maximum Score: {max(framedData.Score)}')

# Rename the column
framedData.rename(columns = {'Score' : 'Exam_Score'}, inplace = True)

# Adding new column
framedData['Promoted'] = framedData['Exam_Score'] > 60
print(f'\nThe new table is  \n{framedData}')

# print(Result)