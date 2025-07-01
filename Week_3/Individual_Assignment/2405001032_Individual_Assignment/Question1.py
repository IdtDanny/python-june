import pandas as pd

data = pd.read_csv('Real Estate.csv')

# Delete column latitude and longitude
data.drop('Latitude', axis = 1, inplace = True)
data.drop('Longitude', axis = 1, inplace = True)

# Filter and show products that sold more than 100,000
product = data['Price'] > 100000

# Export to csv
data.to_csv('New Real Estate.csv', index = False)

# Count streets with type Residential
residentialCount = sum(data['Type'] == 'Residential')

print(f'The Streets with Residential Type are {residentialCount} Streets.')