# counting sort
from collections import defaultdict

def counting_sort(A, key:lambda x: x):
    B, C = [], defaultdict(list)				# output and "counts"
    for x in A:									
        C[key(x)].append(x)						# "count" key(x)
    for k in range(min(C), max(C)+1):			# For every key in the range
        B.extend(C[k])							# Add values in sorted order
    return B

array = [9, 0, 5, 1, 7]
print(counting_sort(array))			#to fix later