import cProfile
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 8, 2, 3]))

#cProfile is will print out timing results about the various
# functions in your program
seq = [10, 8, 2, 3]
if __name__ == "__main__":
    cProfile.run('quicksort(seq)') 