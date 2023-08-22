# insertion sort test
# a rather simple version of insertion sort
def ins_sort1(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i-1] < arr[i]:
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr

array_to_sort = [6,9,1,5,0]
print(ins_sort1(array_to_sort))

# a recursive version
def rec_ins_sort(arr, i=None):
    if i is None: i = len(arr)-1
    if i == 0: return
    rec_ins_sort(arr, i-1)
    j = i
    for j in range(i):
        if arr[j] <  arr[i]:
            j += 1
        else:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
    return arr

print(rec_ins_sort(array_to_sort))

# iterative version
def ite_ins_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    
    return arr

# selection sort
def rec_sel_sort(arr, i=None):
    if i is None: i = len(arr)-1
    if i == 0: return
    max_i = i
    for j in range(i):
        if arr[j] > arr[max_i]: max_i = j
    arr[i], arr[max_i] = arr[max_i], arr[i]
    rec_sel_sort(arr, i-1)
    return arr

# iterative version
def ite_sel_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        max_i = i
        for j in range(i):
            if arr[j] > arr[max_i]: max_i = j
        arr[i], arr[max_i] = arr[max_i], arr[i]
    return arr

print(rec_sel_sort(array_to_sort))
print(ite_sel_sort(array_to_sort))

# quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [ i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def ite_quick_sort(arr):
    less = []
    greater = []
    pivot = arr[0]
    for i in range(1,len(arr)):
        #if arr[i] == pivot: continue          # since we will start from the next element this line has been commented out
        if arr[i] > pivot: greater.append(arr[i])
        else: less.append(arr[i])
    return less + [pivot] + greater

print(ite_quick_sort(array_to_sort))
print(quick_sort(array_to_sort))

# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1+i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j] , arr[i]
    return arr

print(bubble_sort(array_to_sort))
    
# recursive version
def rec_bubble_sort_infinite(arr, i=None, var=None):
    if i is None: i = 0
    limit = len(arr)
    var = limit_checker(i, limit)
    rec_bubble_sort(arr, i+1, var)						# To fix RecursionError: maximum recursion depth exceeded in comparison
    while var:
        j = i
        for j in range(i):
            if j > 0 or arr[j-1] < arr[j]:
                j += 1
            else:
                arr[j-1], arr[j] = arr[j] , arr[j-1]
                j -= 1
    return arr

def limit_checker(index, limit):
    if index+1 > limit:
        return False
    else:
        return True

def rec_bubble_sort(arr, i=0):
    if i == len(arr) - 1:
        return arr # Base case
    
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]

    return rec_bubble_sort(arr, i + 1)


print(rec_bubble_sort(array_to_sort))