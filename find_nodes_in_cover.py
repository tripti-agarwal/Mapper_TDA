from cover import *
from filter import *

def insert_nodes_in_overlapped_bins():
	lol_empty=[]
	for i in range(len(overlaped_covers)):
		create_empty_list=[]
		lol_empty.append(create_empty_list)
		
	for i in range(len(filtered_list)):
		x=filtered_list[i][1]
		node_no=filtered_list[i][0]
		node_weight=filtered_list[i][2]
		node=[]
		node.append(node_no)
		node.append(node_weight)
		for j in range(len(overlaped_covers)):
			if x>overlaped_covers[j][0] and x<=overlaped_covers[j][1]:
				lol_empty[j].append(node)
	nodes_in_bins=lol_empty
	return nodes_in_bins       #in each bin we have the node_no and its corresponding weight depending on the filterfunction where it should lie


nodes_in_bins=insert_nodes_in_overlapped_bins()
