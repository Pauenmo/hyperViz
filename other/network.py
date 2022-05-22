"""
Goal: to highlight the relations between 3 or more disciplines, by breaking down the hypergraph into a simple graph
"""

# TODO: make the graph prettier, with colors, sizes and minimizing edge crossings where possible
# TODO: try to make the graph interactive, so that edges and nodes get highlighted when hovering over them

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import itertools

discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']

G = nx.Graph()
G.add_nodes_from(discipline_names)


"""
Extracting the information for the graph
"""

# First step: automatically create the matrix, from the randomly generated sample
# First, we read the csv into a dataframe
data = pd.read_csv('2021.04.24.csv')
# All the disciplines mentioned in the csv will be in this list
# Use the two lines below when reading the disciplines from the csv
total_disciplines = data.loc[:,'Disciplines']
total_disciplines = total_disciplines.tolist()
# When taking a sample from the sample generator, use the following line
# total_disciplines = genSample(15)
    
matrix = [ [ 0 for i in range(len(discipline_names)) ] for j in range(len(discipline_names)) ]


shells = []

for i in range(4,2,-1):
    inner_nodes = []
    for entry in total_disciplines:
        entry = entry.split(';')
        for discipline in entry:
            if discipline not in discipline_names:
                entry.remove(discipline)
        if len(entry) == i:
            node_label = ""
            for d in entry:
                node_label += d[0] + ","
            node_label = node_label[:-1]
            inner_nodes.append(node_label)
            G.add_node(node_label)
            # Uncomment to add edges to the centre
            # for d in entry:
            # G.add_edge(d, node_label)
    if inner_nodes != []:
        shells.append(inner_nodes)

"""
Drawing the graph
"""

shells.append(discipline_names)
# shells = [inner_nodes, discipline_names]
pos = nx.shell_layout(G, shells)

options = {
    'node_color': 'red',
    'node_size': 1500,
    'width': 3,
}

nx.draw(G, pos, with_labels=True, font_weight='bold', **options, **pos)
plt.savefig('network_picture', bbox_inches='tight')


