import random

def binary_search(array, n):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2
        if n < array[mid]:
            high = mid
        elif n > array[mid]:
            low = mid + 1
        else:
            return mid

    return -1


def test_binary_search(n_test_cases, min_size=10, max_size=100):
    if min_size < 10:
        min_size = 10
    successes = 0
    for _ in range(n_test_cases):
        a = sorted(random.sample(range(max_size), random.randint(min_size, max_size)))
        i = random.randint(0, len(a) - 1)
        if i == binary_search(a, a[i]):
            successes += 1

    return (successes, n_test_cases)


def main():
    array = sorted(random.sample(range(10000), 10000))
    print(binary_search(array, array[random.randint(0, len(array) - 1)]))
    print(test_binary_search(2000))

if __name__ == "__main__":
    main()