import pandas as pad

importedData = pad.read_csv('Book.csv')

print(f'\nThe Imported Data are \n{importedData}')

print(f'\nThe max Height is {importedData.Height.max()}')

print(f'The min Height is {importedData.Height.min()}')

print(f'The avg Height is {importedData.Height.mean()}')

print(f'\nThe sum Height is {importedData.Height.sum()}')

# Adding Enough Column
importedData['Enough'] = importedData['Height'] > 160

importedData.to_csv('Export.csv', index=False)