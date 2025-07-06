import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'Product' : ['Apple', 'Banana', 'Orange', 'Mango'],
        'Price' : [100, 40, 60, 80],
        'Quantity' : [30, 50, 40, 10]}

df = pd.DataFrame(data)

df['Total'] = df['Price'] * df['Quantity']

filter_df = df[df['Quantity'] > 30]

print(f'The mean using numpy is: {np.mean(df['Price'])}')
print(f'The other way to find mean is: {df['Price'].mean()}')

print(f'\nFiltered with Quantity > 30: \n{filter_df}')

print(f'\nWhole DataFrame of the Data: \n{df}')

plt.plot(df['Product'] ,df['Price'])
plt.plot(df['Product'], df['Quantity'])

plt.xlabel('Product')
plt.ylabel('Price and Quantity')
plt.title('Product against Price and Quantity ')
plt.legend(['Price', 'Quantity'])
plt.show()

plt.pie(df['Price'], explode=(0.1, 0, 0, 0), labels=df['Product'],autopct='%1.1f%%')
plt.title('Product by Price Distribution')
plt.show()

plt.bar(df['Product'], df['Price'])
plt.show()