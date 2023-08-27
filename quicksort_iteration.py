def ite_quick_sort(arr):
  stack = [(0, len(arr)-1)]
  
  while stack:
    left, right = stack.pop()
    
    if left >= right:
      continue
    
    pivot_idx = partition(arr, left, right)
    stack.append((left, pivot_idx-1)) 
    stack.append((pivot_idx+1, right))

  return arr

def partition(arr, left, right):
  pivot_idx = left
  pivot = arr[pivot_idx]
  
  while left < right:
    while left < right and arr[right] > pivot:
      right -= 1
    arr[left] = arr[right]
    
    while left < right and arr[left] <= pivot:
      left += 1
    arr[right] = arr[left]

  arr[left] = pivot
  return left
array = [9, 8, 6, 4, 3, 1]
print(ite_quick_sort(array))