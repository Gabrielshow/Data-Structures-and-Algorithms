#merge sort

#bubble sort
def sort(arr):
    for i in range(len(arr)):
        for j in range(1+i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr



array = [4, 7, 1,3]

print(sort(array))
def merge(arr, p ,q, r):
    #arr is the array to be given
    #p is the lower bound of the array
    #q is the middle integer of the array
    #r is the upper bound of the array
    #we assume p <= q < r
    #we assume that the arr and its subarrays are sorted
    q = int(len(arr)/2)
    n1 = q - p + 1
    n2 = r - q
    arrL = arr[:n1]
    arrR = arr[n1+1:n2]
    for i in range(1, n1):
        arrL[i] = arr[p + i -1]
    for j in range(1, n2):
        arrR[j] = arr[q + j]
    #arrL[n1 + 1] = inf
    #arrR[n2 + 1] = inf
    i = 1
    j = 1
    k = p
    for k in range(r):
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i = i + 1
        else:
            arr[k] = arrR[j]
            j = j + 1
    return arr


        