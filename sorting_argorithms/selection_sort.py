def selection_sort(arr):
    """
    very simple but inefficient: find the smallest element using a linear scan
    and move it to the front (swap it with the front element). Then repeat this procedure
    until it is sorted.
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)


ar = [4, 2, 2, 5, 7, 3]
selection_sort(ar)
