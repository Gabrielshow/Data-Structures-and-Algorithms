def comb_sort(arr):
    shrink = 1.3
    gaps = len(arr)
    swapped = True
    i = 0
    
    while gaps > 1 or swapped:
        gaps = int(float(gaps)/shrink)
        
        swapped = False
        i = 0
        
        while gaps + i < len(arr):
            if arr[i] > arr[i+gaps]:
                arr[i], arr[i+gaps] = arr[i+gaps], arr[i]
                swapped = True
            i += 1
    return arr
arr = [5,15,37,29,25,79]
print(comb_sort(arr))
        