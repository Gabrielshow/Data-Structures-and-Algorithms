# Another merge sort implementation
def mergeSort(A):
    if len(A) > 1:
        print('splitting', A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        mergeSort(left)
        mergeSort(right)
        
    # 3 initialization operations
        i = j = k = 0
        # Traverse and merges the sorted arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i = i + 1
            else:
                A[k] = right[j]
                j = j + 1
            k = k + 1
        
        while i < len(left):
            A[k] = left[i]
            i = i + 1
            k = k + 1
            
        while j < len(right):
            A[k] = right[j]
            j = j + 1
            k = k + 1
    print('merging ', A)
    return (A)

mergeSort([356, 97, 846, 215])