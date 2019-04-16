import numpy as np
#read vertices data ----follow readme file---------------
with open('TDA_Project_Dataset/outputfile692.txt') as f:
    lines = f.read().splitlines()

data=[]
k=4

for i in range(len(lines)-4):
	data.append(lines[k])
	k+=1

for i in range(len(data)):
	data[i] = data[i].split(',')

data_f1=[]
data_f2=[]
critical_flag=[]
weights=[]

for i in range(len(data)):
	for j in range(len(data[0])):
		if(j==0):
			data_f1.append(data[i][j])			#f1 values
		elif(j==1):
			data_f2.append(data[i][j])		#f2 values
		elif(j==2):
			critical_flag.append(data[i][j])    #critical flags
		elif(j==3):
			weights.append(data[i][j])			#weight of each node

#read adjacency data file-----Here the values in each row represents the adjacent vertex/vertices to the vertex at that particular vertex-----
#first row shows adjacent vertices for vertex 0 and so on.
with open('TDA_Project_Dataset/output_adjacentedges_692.txt') as f2:
	lines_adjacency = f2.read().splitlines()

data_edges=[]

for i in range(len(lines_adjacency)):
	data_edges.append(lines_adjacency[i])
#preprocessing of data
for i in range(len(data_edges)):
	data_edges[i] =  data_edges[i].split(' ')
	data_edges[i] = list(filter(lambda x: x != '', data_edges[i]))

