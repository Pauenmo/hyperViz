"""
See readme.md for more on the project
"""

import pandas as pd
# import matplotlib
# matplotlib.use('MacOSX')
import matplotlib.pyplot as plt   
import matplotlib.ticker as mtick
from sample_generator import *


#First, we read the csv into a dataframe
data = pd.read_csv('finalNN2021.csv')

#To see the headers of the columns:
# headers = data.iloc[0,:]
# print(headers)

#in this test_form, the second row contains all the disciplines
discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']


#All the disciplines mentioned in the csv will be in this list
# Use the two lines below when reading the disciplines from the csv
total_disciplines = data.loc[:,"What disciplines better represent your research activity or interests?"]
total_disciplines = total_disciplines.tolist()
# When taking a sample from the sample generator, use the following line
# total_disciplines = genSample(15)

# This function draws a histogram of the percentage of attendants that mention each discipline
def disciplinePercentage():
    number_of_attendants = 0
    # For each discipline, count the percentage of attendants that mention it
    discipline_percent = {}
    for discipline in discipline_names:
        discipline_percent[discipline] = 0 

    # First, calculate the number of people that mention each discipline
    for entry in total_disciplines:
        number_of_attendants += 1
        for discipline in discipline_names:
            if discipline in entry:
                discipline_percent[discipline] += 1

    # Then, convert it to percentages
    for discipline in discipline_percent.keys():
        discipline_percent[discipline] = discipline_percent[discipline] * 100 / number_of_attendants        
    
    # Rename some fields
    discipline_percent['Cognition'] = discipline_percent.pop('Cognitive Science')
    discipline_percent['Computation'] = discipline_percent.pop('Computer Science')

    # This line is just to order the dictionary (and hence the graph) by descendig value
    discipline_percent = {k: v for k, v in sorted(discipline_percent.items(), reverse=True, key=lambda item: item[1])}

    #Finally, we draw this as a bar chart
    #These first two lines are just to force y labels to be integers
    ax = plt.figure().gca()
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals = 0))
    
    plt.bar(discipline_percent.keys(), discipline_percent.values())
    plt.xticks(rotation = 90)
    plt.ylabel("Percentage of attendants")
    plt.savefig('./final_outputs/people_per_discipline_percentage.png', bbox_inches='tight')


# This function draws the first basic bar chart: number of people in each discipline
def disciplineCount():
    #Dictionary with the disciplines as keys and the number of times they are in the form as values
    discipline_count = {}
    
    for d in discipline_names:
        count = 0
        for entry in total_disciplines:
            count += entry.count(d)
            discipline_count[d] = count
                
    # print("discipline_count: ", discipline_count)

    # Rename some fields
    discipline_count['Cognition'] = discipline_count.pop('Cognitive Science')
    discipline_count['Computation'] = discipline_count.pop('Computer Science')

    # This line is just to order the dictionary (and hence the graph) by descendig value
    discipline_count = {k: v for k, v in sorted(discipline_count.items(), reverse=True, key=lambda item: item[1])}

        
    #Finally, we draw this as a bar chart
    #These first two lines are just to force y labels to be integers
    ax = plt.figure().gca()
    ax.yaxis.get_major_locator().set_params(integer=True)
    
    plt.bar(discipline_count.keys(), discipline_count.values())
    plt.xticks(rotation = 90)
    plt.ylabel("Number of attendants")
    plt.savefig('./final_outputs/people_per_discipline.png', bbox_inches='tight')

#This function draws the basic bar chart of how many people selected each number of disciplines
def disciplineFreq(in_percentage = True):
    #Need to ignore whatever was entered in the 'Other' field
    #frequencies: list where every entry corresponds to an answer and every value to the number of disciplines in it
    frequencies = []
    number_of_entries = 0
    for entry in total_disciplines:
        number_of_entries += 1
        entry = entry.split(";")
        count = 0
        for discipline in entry:
            if discipline in discipline_names:
                count += 1
        if count > 0:
            frequencies.append(count)

    #Finally, we plot this as a bar chart
    keys = list(set(frequencies))
    keys.sort()
    values = []
    for k in keys:
        if in_percentage:
            values.append(frequencies.count(k) * 100/number_of_entries)
        else:
            values.append(frequencies.count(k))

    #These first two lines are just to force y labels to be integers
    ax = plt.figure().gca()
    if in_percentage:
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals = 0))
    ax.yaxis.get_major_locator().set_params(integer=True)
    plt.xticks(range(1, len(discipline_names)))
 
    plt.bar(keys, values)
    plt.xlabel("Number of disciplines")
    if in_percentage:
        plt.ylabel("Percentage of attendants")
        plt.savefig('./final_outputs/number_of_disciplines_percentage.png')
    else:
        plt.ylabel("Number of attendants")
        plt.savefig('./final_outputs/number_of_disciplines.png')


"""
Main program
"""
# disciplineCount()
disciplineFreq(in_percentage=False)
# disciplinePercentage()


# TODO: learn to change a key in a dictionary

# dictionary = {'a': 1, 'b': 2, 'c':3}
# print(dictionary)
# # dictionary['new_key'] = dictionary['a']
# dictionary['new_key'] = dictionary.pop('a')
# print(dictionary)
# # del dictionary['a']
# print(dictionary)
