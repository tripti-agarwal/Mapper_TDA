from filter import *
def get_no_bins(minimum,maximum,N):
	n = (maximum-minimum)/N
	if (n%10!=0):
		n=n+1
		n=n//1
	return n

def get_absolute_covers(minimum,maximum,n):
	abs_covers=[]
	for i in range(int(minimum),int(maximum)+1,int(n)):
		covers=[]
		mini=i
		cover_low=mini
		cover_max=mini+n
		covers.append(cover_low)
		covers.append(cover_max)
		abs_covers.append(covers)
	return abs_covers

def get_overlapped_covers(absolute_covers,p,n):
	epsilon = n * p
	overlaped_covers = []
	for i in range(len(absolute_covers)):
		cover_dashed=[]
		minimum=absolute_covers[i][0]
		maximum=absolute_covers[i][1]
		minimum-=epsilon
		maximum+=epsilon
		cover_dashed.append(minimum)
		cover_dashed.append(maximum)
		overlaped_covers.append(cover_dashed)
	return overlaped_covers

def binning():
	minimum=filter_range[0]
	maximum=filter_range[1]
	bin_covers=[]
	n = get_no_bins(minimum,maximum,N)
	absolute_covers=get_absolute_covers(minimum,maximum,n)
	overlaped_covers=get_overlapped_covers(absolute_covers,p,n)
	return overlaped_covers
	
# bin=(filter.range[1]-filter.range[0])//N
#define covers, find no. of nodes in each cover, then add the filter val of the nodes and the no. of nodes which have been added
N=40   #no. of covers
p=0.8	#overlap = 80%
overlaped_covers=binning();