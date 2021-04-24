"""
Testing around the concept of chord diagrams
"""

from chord import Chord
from sample_generator import *
import itertools


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

total_disciplines = genSample(15)
    
matrix = [ [ 0 for i in range(len(discipline_names)) ] for j in range(len(discipline_names)) ]

for entry in total_disciplines:
    entry = entry.split(';')
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
        
print(matrix)

