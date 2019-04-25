from find_nodes_in_cover import *
import numpy as np

# print nodes_in_bins
def bins_connectivity():
	list_of_nodes_in_bins=[]
	for i in range(len(nodes_in_bins)):
		nodes=[]
		for j in range(len(nodes_in_bins[i])):
			nodes.append(nodes_in_bins[i][j][0])
		list_of_nodes_in_bins.append(nodes)
	#print list_of_nodes_in_bins
	array=np.zeros((N,N),int)
	for i in range(N):
		for j in range(N):
			if(i==j):
				array[i][j]=0
			else:
				array[i][j]=len(list(set(list_of_nodes_in_bins[i]).intersection(list_of_nodes_in_bins[j])))
	return array

bins_connectivity=bins_connectivity()
