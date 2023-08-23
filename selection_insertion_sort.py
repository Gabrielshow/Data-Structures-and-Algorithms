# Recursive insertion sort
def ins_sort_rec(seq, i):
    if i == 0: return		# Base case -- do nothing
    ins_sort_rec(seq, i-1)  # Sort 0..i-1
    j = i                   # Start "walking" down
    while j > 0 and seq[j-1] > seq[j]:  # Look for OK spot
        seq[j-1], seq[j] = seq[j], seq[j-1] # keep moving seq[j] down
        j -= 1              # Decrement j
    
    return seq
        
        

# iterative version
def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1] # keep moving seq[j] down
            j -= 1
            
    return seq

# selection sort recursive version
def sel_sort_rec(seq, i):
    if i == 0: return        # Base case -- do nothing
    max_j = i                # idx. of largest value so far
    for j in range(i):       # Look for a larger value
        if seq[j] > seq[max_j]: max_j = j # Found one? update max_j
    seq[i], seq[max_j] = seq[max_j], seq[i] # Switch largest into place
    sel_sort_rec(seq, i-1)                 # Sort 0..i-1
    

# selection sort iterative version
def sel_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[i] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]
    
