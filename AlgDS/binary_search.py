def binary_search(array, n):
    if len(array) == 1:
        return False
    
    mid = len(array) // 2

    print(mid)
    print(len(array))

    if n < array[mid]:
        return binary_search(array[:mid], n)
    elif n > array[mid]:
        return binary_search(array[mid:], n)
    else:
        return True

def main():
    print(binary_search([1, 2, 3, 4, 5], 4))
    print(binary_search([1, 2, 3, 4, 5], 2))
    print(binary_search([1, 2, 3, 4, 5], 5))
    print(binary_search([1, 2, 3, 4, 5], 66))

if __name__ == "__main__":
    main()