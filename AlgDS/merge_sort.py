import datetime
import random

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

npassed, nfailed = 0, 0
for itest in range(1, 13):
    print('Test case:', itest)
    nelements = random.randint(int((10**(itest/2.))/2), int(10**(itest/2.)))
    print('Array size:', nelements)
    array = [random.randint(1, 100*nelements) for _ in range(nelements)]
    tic = datetime.datetime.now()
    submission = merge_sort(array)
    toc = datetime.datetime.now()
    answer = sorted(array)
    correct = len(submission) == len(answer) and (submission == answer)
    if correct:
        print('PASSED (Runtime = %.2f seconds)' % (toc-tic).total_seconds())
        npassed += 1
    else:
        print('FAILED')
        nfailed += 1
        print(array)
        print(submission)
        print(answer)
    print('='*100)
print('TOTAL PASSED: %d. TOTAL FAILED: %d.' % (npassed, nfailed))