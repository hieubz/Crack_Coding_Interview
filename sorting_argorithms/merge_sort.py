# like quick sort, merge sort is a divide and conquer algorithm
# and have O(nlog(n)) time complexity like quick sort
# space complex: O(n) > worse than quick sort O(log(n))

def merge_sort(arr):
    helper = [0] * len(arr)
    _merge_sort(arr, helper, 0, len(arr) - 1)

    return arr


def _merge_sort(arr, helper, start, end):
    if start < end:
        # divide
        middle = (start + end) // 2

        # conquer
        _merge_sort(arr, helper, start, middle)
        _merge_sort(arr, helper, middle + 1, end)

        # merge
        _merge(arr, helper, start, middle, end)


def _merge(arr, helper, start, middle, end):

    # copy all the elements of array to helper array
    for i in range(start, end + 1):
        helper[i] = arr[i]

    helper_left = start
    helper_right = middle + 1
    current = start

    # iterate through the helper array , compare the left and right half, coping
    # back the smaller element from the two halves into the original array
    while helper_left <= middle and helper_right <= end:
        if helper[helper_left] <= helper[helper_right]:
            arr[current] = helper[helper_left]
            helper_left += 1
        else:
            arr[current] = helper[helper_right]
            helper_right += 1

        # increase current index of original array
        current += 1

    # copy the rest of the left side of the array into the target array
    remaining = middle - helper_left
    for i in range(remaining + 1):
        arr[current + i] = helper[helper_left + i]


if __name__ == '__main__':
    arr = [1, 4, 2, 3, 9]
    print(merge_sort(arr))
