# a simple sequence checker
def sort_w_check(seq):
    n = len(seq)
    for i in range(n-1):
        if seq[i] > seq[i+1]:
            print("Array not Sorted")
            break
    else:
        return
    



    
