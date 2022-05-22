"""
Testing around the concept of chord diagrams
"""

# TODO: make sure that the labels do not get cutoff

from chord import Chord
# from sample_generator import *
import itertools
import pandas as pd


Chord.user = "pauenmo@gmail.com"
Chord.key = "CP-fdc99bda-356e-4947-a76d-2bd4b3cec8d2"

discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']

# utility: cleans list from answers from the 'other' field
def clean(l):
    for e in l:
        if e not in discipline_names:
            l.remove(e)
    
    #check if we are done
    for e in l:
        if e not in discipline_names:
            return clean(l)

    return l

# First step: automatically create the matrix, from the randomly generated sample

#First, we read the csv into a dataframe
#data = pd.read_csv('2021.05.16.csv')
data = pd.read_csv("SS_2022_data.csv")
#All the disciplines mentioned in the csv will be in this list
# Use the two lines below when reading the disciplines from the csv
total_disciplines = data.loc[:,"What disciplines better represent your research activity, work or interests?"]
total_disciplines = total_disciplines.tolist()
# When taking a sample from the sample generator, use the following line
# total_disciplines = genSample(15)
    
# initialise empty matrix
matrix = [ [ 0 for i in range(len(discipline_names)) ] for j in range(len(discipline_names)) ]

for entry in total_disciplines:
    entry = clean(entry.split(';'))
    if len(entry)>=2:
        pairs = list(itertools.combinations(entry, 2))        
        for pair in pairs:
            pair = list(pair)
            pair[0] = discipline_names.index(pair[0])
            pair[1] = discipline_names.index(pair[1])
            # Each person contributes a total of 1, so each pair gets a contribution of 1/(number of pairs)
            # matrix[pair[0]][pair[1]] += 1 / len(pairs)
            # Alternatively, we can just count the number of times each pair appears:
            matrix[pair[0]][pair[1]] += 1
            matrix[pair[1]][pair[0]] += 1
        
# print(matrix)
# Chord(matrix, discipline_names).to_html('2021.05.16-chord_diag.html')

# TODO: for each arity, two different .csv counting number of times mentioned
# 1.- answers with that exact arity
# 2.- answers with arity same or more
# Example, for arity 3, the first csv counts the number of times each threesome of disciplines is mentioned exactly
# And the second csv counts the number of times the threesome gets mentioned in total_disciplines

# test_list = ['Philosophy', 'Complexity', 'Anthropology']
# for arity in range(1, len(test_list)+1):
#     items = list(itertools.combinations(test_list, arity))
#     print(items)

"""
Writing to csv
"""
import csv


# my_dict = {('Philosophy', 'Complexity', 'Anthropology'):2,  'aaa':1, '2': 'bbb', '3': 'ccc'}
# with open('./exact_csvs/test.csv', 'w') as f:
#     for key in my_dict.keys():
#         f.write("%s,%s\n"%(key,my_dict[key]))


# this generates all the exact dictionaries of all the possible arities
def genExactDicts():
    for arity in range(1, len(discipline_names)+1):
        exact_dict = {}
        tuples = list(itertools.combinations(discipline_names, arity))
        for tuple in tuples:
            exact_dict[tuple] = 0
        for entry in total_disciplines:
            entry = clean(entry.split(";"))
            if len(entry) == arity:
                entry_tuples = list(itertools.combinations(entry, arity))
                for t in entry_tuples:
                    exact_dict[t] += 1
        #filename = './final_outputs/exactDict-arity-' + str(arity) + '.csv'
        filename = './SS_2022/exactDict-arity-' + str(arity) + '_SS_2022.csv'
        with open(filename, 'w') as f:
            for key in exact_dict.keys():
                f.write("%s,%s\n"%(key,exact_dict[key]))

# this generates all the cumulative dictionaries of all the possible arities
def genCumulativeDicts():
    for arity in range(1, len(discipline_names)+1):
        cumulative_dict = {}
        tuples = list(itertools.combinations(discipline_names, arity))
        for tuple in tuples:
            cumulative_dict[tuple] = 0
        for entry in total_disciplines:
            entry = clean(entry.split(";"))
            if len(entry) >= arity:
                entry_tuples = list(itertools.combinations(entry, arity))
                for t in entry_tuples:
                    cumulative_dict[t] += 1
            #filename = './final_outputs/cumulativeDict-arity-' + str(arity) + '.csv'
            filename = './SS_2022/cumulativeDict-arity-' + str(arity) + 'SS_2022.csv'
            with open(filename, 'w') as f:
                for key in cumulative_dict.keys():
                    f.write("%s,%s\n"%(key,cumulative_dict[key]))

genExactDicts()
genCumulativeDicts()

# TODO: program reality checks for these functions!




    
