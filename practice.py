# sorting algorithms spaced repetition, leitner method
def gnomesort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i-1] < arr[i]:
            i += 1
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

arr = [1,9,5,7]
print(gnomesort(arr))