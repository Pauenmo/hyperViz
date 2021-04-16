"""
Functions to generate random samples: lists of subsets of disciplines

These samples are to test the concept of chord diagrams
"""

import random

discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']


#First approach: completely random
#Later on, we can have tweakable probability parameters to get more reasonable samples

#This function generates a random sample
def genSample(size):
    sample = []   
    for a in range(size):
        #First, choose a number of disciplines at random
        n = random.randint(1,len(discipline_names))
        answer = []
        #Then, we choose randomly n disciplines, checking to not choose the same twice
        for i in range(n):
            candidate = random.randint(0, len(discipline_names)-1)
            while discipline_names[candidate] in answer:
                candidate = random.randint(0, len(discipline_names)-1)
            answer.append(discipline_names[candidate])
        sample.append(answer)
    return sample


#Main program: where we can test the functions
if __name__=="__main__":
    size = 5
    sample = genSample(size)
    for s in sample:
        print(s, "\n")
        




