from connectivity_bins import *
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from(vertex_list)
G.add_edges_from(edge_list)
nx.draw(G)
plt.show()