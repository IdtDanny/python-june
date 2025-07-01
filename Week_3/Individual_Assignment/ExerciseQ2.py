import pandas as pd,numpy as pe, matplotlib.pyplot as plt
#A teacher has recorded exam results for students in a CSV file with the columns. Create a python program to make a data frame with at least 10 students with Student_ID, Name, Math, English, Science
#1. display dataframe
result={"Student_ID":[2501,2502,2503,2504,2505,2506,2507,2508,2509,2510],"Name":["Danny","Gogo","straton","Keza","Karabo","Akazuba","Jordan","Isimbi","Teddy","Uwera"],
        "Math":[80,50,60,70,90,92,95,50,55,69],"English":[70,90,70,80,99,79,87,76,89,59],"Science":[90,68,79,76,85,97,83,63,75,54]}
output=pd.DataFrame(result)
print(output)
output['average'] = output[['Math','English','Science']].mean(axis=1)
print(f'\n{output}')
output['Status']=pe.where(output['average']>=50,'Pass','Fail')
print(f'\n{output}')
output= output.sort_values(by='average', ascending=False)
print(f'\n{output}')
print(f'\n{output.head(3)}')
"""
x=output['Student_ID']
y_math=output['Math']
y_english=output['English']
y_science=output['Science']
plt.plot(x,y_math,'o-',label='Math')
plt.plot(x,y_english,'o-',label='English')
plt.plot(x,y_science,'o-',label='Science')
plt.title('Student Performance')
plt.xlabel('Student ID')
plt.ylabel('Scores')
plt.legend()
plt.show()
"""
A = output['Math']
labels = output['Name']

plt.figure(figsize=(10, 7))
plt.pie(A, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Math Performance')
plt.axis('equal')
plt.legend()
plt.show()
