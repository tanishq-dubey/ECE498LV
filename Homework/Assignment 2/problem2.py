import networkx as nx
from networkx.algorithms import bipartite
from networkx.algorithms import coloring
import matplotlib.pyplot as plt
G = nx.Graph()

# Read and cleanup data
lines = [line.rstrip('\n') for line in open("out.opsahl-southernwomen")]
lines = [list(filter(None, line.split(" "))) for line in lines]
lines = [(int(line[0]), line[1]) for line in lines]

# Build the graph
G.add_edges_from(lines)

# Find the chromatic number (part A)
colors = coloring.greedy_color(G)
colorsUq = {}
for node in colors:
    if colors[node] not in colorsUq:
        colorsUq[colors[node]] = 1
print(len(colorsUq)) # Find the unique number of colors and print

# Split into the bipartite sets
women, events = bipartite.sets(G)
WG = bipartite.projected_graph(G, women)
EG = bipartite.projected_graph(G, events)

# Draw all 3 graphs on the same plot (parts B and C)
plt.subplot(131)
nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.subplot(132)
nx.draw_circular(WG, with_labels=True, font_weight='bold')
plt.subplot(133)
nx.draw_circular(EG, with_labels=True, font_weight='bold')

