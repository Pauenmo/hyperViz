"""
Testing around the concept of chord diagrams
"""

from chord import Chord
from sample_generator import *
import itertools
import pandas as pd


Chord.user = "pauenmo@gmail.com"
Chord.key = "CP-fdc99bda-356e-4947-a76d-2bd4b3cec8d2"

discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']

# Basic chord diagram, for reference

# matrix = [
#     [0, 5, 6, 4, 7, 4],
#     [5, 0, 5, 4, 6, 5],
#     [6, 5, 0, 4, 5, 5],
#     [4, 4, 4, 0, 5, 5],
#     [7, 6, 5, 5, 0, 4],
#     [4, 5, 5, 5, 4, 0],
# ]

# names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]

# Chord(matrix, names).to_html('out.html')



# First step: automatically create the matrix, from the randomly generated sample

#First, we read the csv into a dataframe
data = pd.read_csv('2021.04.24.csv')
#All the disciplines mentioned in the csv will be in this list
# Use the two lines below when reading the disciplines from the csv
total_disciplines = data.loc[:,'Disciplines']
total_disciplines = total_disciplines.tolist()
# When taking a sample from the sample generator, use the following line
# total_disciplines = genSample(15)
    
matrix = [ [ 0 for i in range(len(discipline_names)) ] for j in range(len(discipline_names)) ]

for entry in total_disciplines:
    entry = entry.split(';')
    for discipline in entry:
        if discipline not in discipline_names:
            entry.remove(discipline)
    if len(entry)>2:
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
        
print(matrix)

Chord(matrix, discipline_names).to_html('testing.html')

