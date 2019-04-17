from read_data import data_f1,data_f2,weights,critical_flag,data_edges
import math
#filter function by using the formula eigen function from graph laplacian from MOG paper  by Mustafa Hajij

def filter_range():
	filtered_list = my_filter()
	filtered_list.sort(key = lambda filtered_list: filtered_list[1])    #sort list according to filter_val
	filter_range=[]
	minimum=filtered_list[0][1]
	maximum=filtered_list[len(filtered_list)-1][1]
	filter_range.append(minimum)
	filter_range.append(maximum)
	return filter_range
def my_filter():
	filter_lol=[]
	for i in range(len(adjacent_vertices)):
		val = 0.0
		filter_value_list=[]
		for j in range(len(adjacent_vertices[i])):
			
			val+=abs(int(f1[i])-int(f1[int(adjacent_vertices[i][j])]))+abs(int(f2[i])-int(f2[int(adjacent_vertices[i][j])]))
		filter_value_list.append(i)
		filter_value_list.append(val)
		filter_value_list.append(int(weight[i]))
		filter_lol.append(filter_value_list)						
	return filter_lol


f1=data_f1
f2=data_f2
weight=weights
adjacent_vertices=data_edges
filter_range = filter_range()	
