import datetime
import random

def simple_sort(a : list):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a


npassed, nfailed = 0, 0

for itest in range(1, 5):
    print('Test case:', itest)
    nelements = random.randint(int((10**(itest/2.))/2), int(10**(itest/2.)))
    print('Array size:', nelements)
    array = [random.randint(1, 100*nelements) for _ in range(nelements)]
    tic = datetime.datetime.now()
    submission = simple_sort(array)
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