def sentinel_linear_search(arr, x):
    if len(arr) > 0: 
        n = len(arr)-1
        last = arr[-1]
        arr[-1] = x
        i = 0
        while arr[i] != x:
            i += 1
        arr[-1] = last
        if i < n or arr[n] == x:
            return i
        else:
            print("Element not found")
            return -1
        
    else:
        print("Not a valid array")
        return -1


array = [3, 5, 7, 1, 2, 4]
result = sentinel_linear_search(array, 8)
print(result)
        
    
    