def rec_ins_sort(arr, i):
    if i == 0: return
    rec_ins_sort(arr, i-1)
    j = i
    while j == 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    return arr