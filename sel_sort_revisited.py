# selection sort revisited
def sel_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

array = [2, 9 , 1, 0, 3]
print(sel_sort(array))