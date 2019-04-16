from read_data import data_f1,data_f2,weights,critical_flag,data_edges
import math
#filter function by using the formula eigen function from graph laplacian from MOG paper  by Mustafa Hajij
def my_filter(f1,f2,adjacent_vertices,weight):
	filter_lol=[]
	for i in range(len(adjacent_vertices)):
		val = 0.0
		filter_value_list=[]
		for j in range(len(adjacent_vertices[i])):
			
			val+=abs(int(f1[i])-int(f1[int(adjacent_vertices[i][j])]))+abs(int(f2[i])-int(f2[int(adjacent_vertices[i][j])]))
		filter_value_list.append(val)
		filter_value_list.append(int(weight[i]))
		filter_lol.append(filter_value_list)					#storing values in format <filter_val,weight> for each node


def main():
	f1=[]
	f2=[]
	adjacent_vertices=[]
	weight=[]
	f1=data_f1
	f2=data_f2
	weight=weights
	adjacent_vertices=data_edges
	
	my_filter(f1,f2,adjacent_vertices,weight)


if __name__=='__main__':
	main()
