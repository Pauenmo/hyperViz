"""
Testing around the concept of chord diagrams
"""

# TODO: make sure that the labels do not get cutoff

# from hyperViz import disciplineCount
from chord import Chord
from sample_generator import *
import itertools
import pandas as pd


Chord.user = "pauenmo@gmail.com"
Chord.key = "CP-fdc99bda-356e-4947-a76d-2bd4b3cec8d2"

discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']

discipline_names_renamed = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognition',
                    'Biology', 'Education', 'Computation']

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
data = pd.read_csv('finalNN2021.csv')
#All the disciplines mentioned in the csv will be in this list
# Use the two lines below when reading the disciplines from the csv
total_disciplines = data.loc[:,"What disciplines better represent your research activity or interests?"]
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


# discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
#                     'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
#                     'Biology', 'Education', 'Computer Science']


hex_colors = ["#ff0000", "#80ff00", "#0040ff", "#ff9305", "#8000ff", "#19e36d", "#b51f71", "#c99c30", "#02ddfa", "#0a0a0a", "#ddff00"]
Chord(matrix, discipline_names_renamed, colors=hex_colors, padding=0.15,font_size_large="15.4px", width=600).to_html('./final_outputs/chord_diagram.html')
