def two_sum(arr, target):
    l, r = 0, len(arr) - 1

    while l < r:
        sums = arr[l] + arr[r]
        if sums < target:
            l += 1
        elif sums > target:
            r -= 1
        else:
            return [l + 1, r + 1]


arr = [2, 7, 11, 15]
print(two_sum(arr, 9))