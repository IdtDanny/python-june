import matplotlib.pyplot as plt

name = ['Storage', 'Collaboration', 'Digital Power', 'DataCom', 'Campus Network']

ratings = [23.3, 43.5, 12.5, 65.7, 54.3]

customer = [50, 100, 20, 220, 650]

plt.plot(name, ratings)
plt.plot(name, customer)

plt.title('Solutions Favorites')

plt.xlabel('Solution Name')
plt.ylabel('Ratings')

plt.legend(['Ratings', 'Customers * 1k'])

plt.show()