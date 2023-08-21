def counting_sort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    
    for i in range(0, size):
        count[arr[i]] += 1
    
    for j in range(1, 10):
        count[j] += count[j-1]
    
    a = size - 1
    while a >= 0:
        output[count[arr[a]-1]] = arr[a]
        count[arr[a]] -= 1
        a -= 1
    
    for k in range(0, size):
        arr[k] = output[k]
    return arr


l1 = [4,2,2,8,3,3,1]
print(counting_sort(l1))