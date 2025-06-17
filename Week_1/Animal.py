# 3. list of animal: Goat, chicken, sheep, lion, hare
# sort, update list by adding elephant, place wild and domestic asides, add tiger in miffle of wild animals list 
animal = ['Goat', 'Chicken', 'Sheep', 'Lion', 'Hare']
animal.sort()
animal.append("Elephant")

print(f"Sorted animals {animal}")

wild = [animal[2], animal[3], animal[5]]
domestic = [animal[0], animal[1], animal[4]]

wild.insert(1, 'Tiger')

print(f"Wild animals are {wild}")
print(f"Domestic animals are {domestic}")