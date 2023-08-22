def gnomesort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i-1] < arr[i]:
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

def insertion_sort_rec(arr, i=None):
    if i is None: i = len(arr)
    if i == 0: return
    insertion_sort_rec(arr, i-1)
    j = i
    for j in range(i):
        if j > 0 or arr[j-1] < arr[j]:
            j += 1
        else:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

def insertion_sort_ite(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

def selection_sort_rec(arr, i=None):
    if i is None: i = len(arr)
    if i == 0: return
    max_index = i
    for j in range(i):
        if arr[j] > arr[max_index]: max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]
    selection_sort_rec(arr, i-1)
    return arr

def selection_sort_ite(arr):
    for i in range(len(arr)-1, 0, -1):
        max_index = i
        for j in range(i):
            if arr[j] > arr[max_index]: max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
    
# quick sort
def quick_sort(arr):
    if len(arr) < 2: return
    else:
        pivot = arr[0]
        less = [ i for i in arr[1:] if i <= pivot]
        greater = [ i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    return arr

# iterative version of quicksort
# def quick_sort_ite(arr):
#     seq = arr
#     less = []
#     greater = []
#     j = 0
#     for j in range(len(seq)):
#         pivot = seq[0]
#         for i in range(1,len(arr)):
#         #if arr[i] == pivot: continue          # since we will start from the next element this line has been commented out
#             if arr[i] > pivot: greater.append(seq[i])
#             else: less.append(seq[i])
#         seq = less + [pivot] + greater
#         j += 1
#     return seq

# bubble sort
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubblesort_rec(arr, i=None):
    if i is None: i = 0
    if i == len(arr)-1: return arr
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    return bubblesort_rec(arr, i+1)
    
# def double_pivot_quick_sort(arr):
#     if len(arr) < 1: return
#     else:
#         left_index = 0
#         right_index = len(arr)-1
#         for i in range(len(arr)):
#             if left_index < right_index :
#                 if arr[left_index] < arr[right_index] and left_index < right_index:
#                     left_index += 1
#                 arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
#                 if arr[left_index] > arr[right_index] and left_index < right_index:
#                     right_index += 1
#                 arr[left_index], arr[right_index] = arr[right_index], arr[left_index]             
#     return arr

array = [5, 10, 1,7,6,9,0]
print(double_pivot_quick_sort(array))
    