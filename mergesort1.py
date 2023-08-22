# mergesort
def mergesort1(arr):
    if len(arr) < 2: return
    else:
        mid = int(len(arr)/2)
        left_half = arr[:mid]
        right_half = arr[mid:]
        C = mergesort1(left_half)
        D = mergesort1(right_half)
    return C, D

def Merge(C, D):
    i = 0
    j = 0
    B = []
    c_length = len(C)
    d_length = len(D)
    greater_length = 0
    if c_length > d_length:
        greater_length = c_length
    else:
        greater_length = d_length
    for k in range(0, greater_length):
        if C[i] < D[j]:
            B[k] = C[i]
            i += 1
        else:
            B[k] = D[j]
            j += 1
            
    return B
array = [0,5,7,6,2,3,4,1]
print(mergesort1(array))
# To fix this array
            
        
    