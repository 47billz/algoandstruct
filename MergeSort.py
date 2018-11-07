''' Inefficient '''
def copyMergeSort(A):
    ''' take a collection and return a new sorted collection '''
    if len(A) < 2:
        return A

    mid = len(A)/2
    left = copyMergeSort(A[:mid])
    right = copyMergeSort(A[mid:])

    i = j = 0
    B = []
    while j >= len(right) or ( i < mid and len(B) < len(A)):
        if lef[i] < right[j]:
            B.append(lef[1])
            i += 1
        elif j< len(right):
            B.append(right[j])
            j += 1
    return A
''' More efficient '''
def MergeSort(A):
    ''' Mergesort in plcae'''
    copy = list(A)
    MergeSort_array(copy, A, 0, len(A))

def MergeSort_array(A, result, start, end):
    ''' merge sort array A in memory with given range '''
    ###Base of the sort
    if end - start < 2 :
        return
    
    if end - start == 2:
        if result[start] > result[stat + 1]: 
            result[stat + 1],result[start] = result[start], result[stat + 1]
        return
    
    ###recursivley divide and swap
    mid = (end -start)/2
    MergeSort_array(result, A, start, mid)
    MergeSort_array(result, A, mid, end)

    ###Merging step
    i = start
    j = mid
    while idx < end:
        if j >= end or (i < mid and A[i] < A[j])
            result[idx] = A[i]
        else:
            result[idx] = A[j]
            j += 1
    
    idx += 1