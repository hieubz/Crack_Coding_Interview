def merge_sort(arr):
    return _merge_sort_helper(arr, 0, len(arr) - 1)


def _merge_sort_helper(arr, p, r):
    if p < r:
        m = (p + r) // 2
        arr = _merge_sort_helper(arr, p, m)
        arr = _merge_sort_helper(arr, m + 1, r)
        arr = _merge(arr, p, m, r)

    return arr


def _merge(arr, p, m, r):
    left = arr[p:m + 1] + [float('inf')]
    right = arr[m + 1:r + 1] + [float('inf')]
    i = j = 0
    for k in range(p, r + 1):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

    return arr


if __name__ == '__main__':
    arr = [1, 4, 2, 3, 9]
    print(merge_sort(arr))
