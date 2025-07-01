import pandas as pd, numpy as np, matplotlib.pyplot as plt

data = {'Student_ID':[2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415],
        'Name':['Danny', 'Paul', 'Manzi', 'David', 'Gloria', 'Straton', 'Ange', 'Devis', 'Tom', 'Tim'],
        'Math':[89, 85, 75, 96, 78, 81, 78, 34, 76, 70],
        'English':[78, 65, 85, 75, 78, 65, 78, 34, 83, 81],
        'Science':[86, 79, 74, 73, 89, 71, 78, 23, 83, 74]
        }

exam_result = pd.DataFrame(data)

# Describe dataframe
print(f'Dataframe description: \n{exam_result.describe()}')

# Average for all subject
math = np.mean(data['Math'])
english = np.mean(data['English'])
science = np.mean(data['Science'])
print(f'\nMath mean: {math} \nEnglish mean: {english} \nScience mean: {science}')

# Average for every student
exam_result['Average'] = round((exam_result[['Math', 'English', 'Science']].mean(axis=1)), 2)

# Adding new column 'Status' label 'Pass' if average >= 50 otherwise Fail

for i in range(10):
    if exam_result.Average[i] >= 50:
        exam_result['Status'] = 'Pass'
    else:
        exam_result['Status'] = 'Fail'

print(f'\n{exam_result}')


# Visualize your data with line graph Name against Math, English and Science. Add possible chart elements ( titles, labels, legends, etc)
plt.title('Exam Results')

plt.plot(exam_result['Name'], exam_result['Math'], label='Math')
plt.plot(exam_result['Name'], exam_result['English'], label='English')
plt.plot(exam_result['Name'], exam_result['Science'], label='Science')

plt.legend(['Math', 'English', 'Science'])

plt.show()

