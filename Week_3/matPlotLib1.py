import matplotlib.pyplot as plt

name = ['Danny' , 'Straton', 'Ange', 'Gloria']

python = [90, 92, 93, 95]

linear = [98, 91, 96, 91]

plt.plot(name, python)
plt.plot(name, linear)

# Adding title
plt.title('Name vs Score in Python and Linear')

# Adding Labels
plt.xlabel('Names')
plt.ylabel('Score')

# Adding Legend
plt.legend(['Python', 'Linear'])

plt.show()