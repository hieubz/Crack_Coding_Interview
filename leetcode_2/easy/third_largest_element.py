"""
given an array of n integers, find the third largest element
"""


def get_third_largest_ele(arr):
    max1, max2, max3 = arr[0], arr[0], arr[0]

    for num in arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

    return max3


arr = [2, 4, 5, 6, 8, 9, 10, 17]
num = get_third_largest_ele(arr)
print(num)