def find_second_largest_number(arr):
    max_1 = max(arr[0], arr[1])
    max_2 = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max_1:
            max_2 = max_1
            max_1 = arr[i]
        elif arr[i] > max_2 and arr[i] != max_1:
            max_2 = arr[i]

    return max_2


a = [10, 3, 4, 7, 8]
print(find_second_largest_number(a))
