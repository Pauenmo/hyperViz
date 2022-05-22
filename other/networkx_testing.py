import networkx as nx
import matplotlib.pyplot as plt

discipline_names = ['Philosophy', 'Complexity', 'Anthropology', 'Physics',
                    'Linguistics', 'Arts', 'Mathematics', 'Cognitive Science',
                    'Biology', 'Education', 'Computer Science']

G = nx.Graph()
G.add_nodes_from(discipline_names)

options = {
    'node_color': 'red',
    'node_size': 1500,
    'width': 3,
}

# TODO: test if I can decide the precise position of the nodes
# pos = {'Philosophy': (0,0), 'Complexity': (10,0), 'Cognitive Science': (10,10)}

inner_nodes = ['Philosophy', 'Complexity', 'Anthropology']

shells = [discipline_names]
pos = nx.shell_layout(G, shells)

nx.draw_networkx_nodes(G, pos, nodelist=inner_nodes, with_labels=True, font_weight='bold', **options)
plt.savefig('network_testing', bbox_inches='tight')


