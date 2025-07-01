#A Real estate company keeps daily data in an excel file
"""
Using pandas:
1.	Read the sales data file.
2.	Delete two columns latitude and longitude
3.	Filter and show products that sold more than 100 000.
4.	Export the updated data to a new CSV file.
5.	How many streets with type “Residential”
"""
#Read the sales data file
import pandas as pa
data=pa.read_csv('realestate.csv')
#print(data)
#Delete
new_data=data.drop("Latitude",axis=1,inplace=True)
new_data=data.drop("Longitude",axis=1)
#print(new_data)
p=data['Price']>100000
#print(p)
data.to_csv("realestate_updated",index=False)
t=(data['Type']=='Residential').sum()
print(f'The Street with Residential are:is{t}')
