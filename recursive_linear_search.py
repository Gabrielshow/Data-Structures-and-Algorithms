# thomas cormen algorithm unlocked
def recursive_linear_search(arr, x, i= 0):
    n = len(arr)-1
    if i > n:
        return "Not found"
    if arr[i] == x:
        print(f"Element found at index {i}")
        return i
    else:
        return recursive_linear_search(arr, x, i+1)
        

array = [2, 4, 6, 9, 10]
answer = recursive_linear_search(array, 0)
print(answer)
    