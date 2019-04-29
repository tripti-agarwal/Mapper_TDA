from find_nodes_in_cover import *
import numpy as np


def bins_connectivity():
	list_of_nodes_in_bins=[]
	for i in range(len(nodes_in_bins)):
		nodes=[]
		for j in range(len(nodes_in_bins[i])):
			nodes.append(nodes_in_bins[i][j][0])
		list_of_nodes_in_bins.append(nodes)

	array=np.zeros((len(list_of_nodes_in_bins),len(list_of_nodes_in_bins)),int)
	for i in range(len(list_of_nodes_in_bins)):
		for j in range(len(list_of_nodes_in_bins)):
			if(i==j):
				array[i][j]=0
			else:
				array[i][j]=len(list(set(list_of_nodes_in_bins[i]).intersection(list_of_nodes_in_bins[j])))

	return array,list_of_nodes_in_bins



def final_edges_list():
	edge_list=[]
	for i in range(len(bins_connectivity)):
		for j in range(len(bins_connectivity[i])):
			edge_tuple=()
			if(bins_connectivity[i][j]!=0):
				edge_tuple=(i,j,bins_connectivity[i][j])
				edge_list.append(edge_tuple)
	
	return edge_list



def final_vertex_list():
	vertex_list=[]
	for i in range(len(bins_connectivity)):
		vertex_list.append(i)
	return vertex_list


bins_connectivity,list_of_nodes_in_bins=bins_connectivity()
edge_list=final_edges_list()
vertex_list=final_vertex_list()
