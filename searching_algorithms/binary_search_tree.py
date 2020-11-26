def binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid

    return -1


def binary_search_recursive(array, value, low, high):
    if low > high:
        return - 1

    mid = (low + high) // 2
    if array[mid] > value:
        return binary_search_recursive(array, value, low, mid - 1)
    elif array[mid] < value:
        return binary_search_recursive(array, value, mid + 1, high)
    else:
        return mid


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search_recursive(arr, 3, 0, 7))
