"""
See readme.md for more on the project
"""

import pandas as pd
import matplotlib.pyplot as plt


#First, we read the csv into a dataframe
data = pd.read_csv('Test_Form.csv')

#To see the headers of the columns:
# headers = data.iloc[0,:]
# print(headers)

#in this test_form, the second row contains all the disciplines
disciplines = data.loc[2,'Disciplines']
x = disciplines.split(";")

#All the disciplines mentioned in the csv will be in this list
total_disciplines = data.loc[:,'Disciplines']
total_disciplines = total_disciplines.tolist()

#Dictionary with the disciplines as keys and the number of times they are in the form as values
discipline_count = {}

#First, we initialise it to zero for each discipline
for d in x:
    discipline_count[d] = 0

#Then, we assign the proper values to the dictionary
for discipline in discipline_count.keys():
    count = 0
    for entry in total_disciplines:
        count += entry.count(discipline)
    discipline_count[discipline] = count
   
print("discipline_count: ", discipline_count)

#Finally, we draw this as a bar chart
#These first two lines are just to force y labels to be integers
ax = plt.figure().gca()
ax.yaxis.get_major_locator().set_params(integer=True)

plt.bar(discipline_count.keys(), discipline_count.values())
plt.xticks(rotation = 90)

#Graph 2: basic bar chart of how many people selected each number of disciplines
#Need to ignore whatever was entered in the 'Other' field
#frequencies: list where every entry corresponds to an answer and every value to the number of disciplines in it
frequencies = []
for entry in data.loc[:,'Disciplines']:
    entry = entry.split(";")
    count = 0
    for discipline in entry:
        if discipline in discipline_count.keys():
            count += 1
    if count > 0:
        frequencies.append(count)
    
print("frequencies: ", frequencies)

#Finally, we plot this as a bar chart
keys = list(set(frequencies))
keys.sort()
values = []
for k in keys:
    values.append(frequencies.count(k))

#These first two lines are just to force y labels to be integers
ax = plt.figure().gca()
ax.yaxis.get_major_locator().set_params(integer=True)
plt.bar(keys, values)



