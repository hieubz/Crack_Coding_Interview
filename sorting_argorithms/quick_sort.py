def partition_last(arr, low, high):
    """
    divide the arr to 2 parts
    :param arr:
    :param low:
    :param high:
    :return: pivot
    """
    # temp index
    temp = low - 1

    # choose the last one as the pivot
    pivot = arr[high]  # arr[low]

    for j in range(low, high):
        if arr[j] <= pivot:
            # assign index of number (larger than pivot) to temp
            temp += 1
            # swap arr[j] with that larger number
            # intend to move the smaller number to the left side and vise versa
            arr[temp], arr[j] = arr[j], arr[temp]

    # insert pivot number to the middle
    arr[temp + 1], arr[high] = arr[high], arr[temp + 1]

    # return pivot index

    return temp + 1


def partition_start(arr, start, end):
    i = start + 1
    pivot = arr[start]

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # insert pivot element to the middle of two parts
    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    return i - 1


def partition_middle(arr, low, high):
    """
    divide the arr to 2 parts
    :param arr:
    :param low:
    :param high:
    :return: pivot
    """

    # choose the last one as the pivot
    pivot = arr[(low + high) // 2]

    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    return low


def quick_sort(arr, low, high):
    """
    :param arr: array to be sorted
    :param low: starting index
    :param high: ending index
    :return:
    """
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition_last(arr, low, high)

        if low < pi - 1:
            quick_sort(arr, low, pi - 1)
        if pi < high:
            quick_sort(arr, pi + 1, high)  # when use partition_middle:  quick_sort(arr, pi, high)

    return arr


a = [1, 2, 3, 5, 3, 12, 4]
print(quick_sort(a, 0, len(a) - 1))
