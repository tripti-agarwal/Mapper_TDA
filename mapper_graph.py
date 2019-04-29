from connectivity_bins import *

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from(vertex_list)
G.add_weighted_edges_from(edge_list)

print "---------------------------------------------------------------------"
print list_of_nodes_in_bins[0]
print "---------------------------------------------------------------------"

print "---------------------------------------------------------------------"
print list_of_nodes_in_bins[1]
print "---------------------------------------------------------------------"


print "---------------------------------------------------------------------"
print list_of_nodes_in_bins[2]
print "---------------------------------------------------------------------"


print "---------------------------------------------------------------------"
print list_of_nodes_in_bins[3]
print "---------------------------------------------------------------------"


print "---------------------------------------------------------------------"
print list_of_nodes_in_bins[4]
print "---------------------------------------------------------------------"


print "---------------------------------------------------------------------"
print list_of_nodes_in_bins[5]
print "---------------------------------------------------------------------"

index = 2 
weight_list = [x[index]*10 for x in edge_list]
labels={}
for i in range(len(list_of_nodes_in_bins)):
	labels[i]=list_of_nodes_in_bins[i]

#nx.draw_networkx_labels(G,pos,labels,fontsize=1)
nx.draw(G,node_size=weight_list,with_labels=True)

plt.show()