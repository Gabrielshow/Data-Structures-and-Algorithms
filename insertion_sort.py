#insertion sort
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        #insert a[j] into the sorted sequence arr[1..j-1]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
            
        arr[i + 1] = key
        
    return arr

array_to_sort = [9, 0, 4, 7, 8]
print(insertion_sort(array_to_sort))

#Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.
def insertion_sort_right(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
            
        arr[ i + 1] = key
        
    return arr

print(insertion_sort_right(array_to_sort))