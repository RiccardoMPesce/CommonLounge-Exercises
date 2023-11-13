# merge_sort.py 
def merge_sort(array):
    if len(array) <= 1:
        return array 
    low = 0
    high = len(array)
    mid = (high + low) // 2

    left = merge_sort(array[low:mid])
    right = merge_sort(array[mid:high])
    
    return merge(left, right)

def merge(left, right):
    merged = list()
    ii, jj = 0, 0 
    
    while ii < len(left) and jj < len(right):
        if left[ii] <= right[jj]:
            merged.append(left[ii]) 
            ii += 1
        else:
            merged.append(right[jj]) 
            jj += 1

    while ii < len(left):
        merged.append(left[ii]) 
        ii += 1

    while jj < len(right):
        merged.append(right[jj])  
        jj += 1
    
    # check if pointers have reached the end of the list 
    assert ii == len(left)
    assert jj == len(right)
    return merged

array = [5, 10, 8, 7, 3, 7, 6, 12, 2, 7]
result = merge_sort(array)
assert result == [2, 3, 5, 6, 7, 7, 7, 8, 10, 12], result