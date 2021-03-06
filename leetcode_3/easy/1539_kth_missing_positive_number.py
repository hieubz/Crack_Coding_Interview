class Solution:
    # On
    def findKthPositive(self, arr, k):
        set_arr = set(arr)
        max_ele = arr[-1]
        for i in range(1, max_ele + 1 + k):
            if i not in set_arr:
                k -= 1
                if k == 0:
                    return i

        return None

    # Ologn
    def findKthPositive_2(self, arr, k):
        beg, end = 0, len(arr)

        while beg < end:
            mid = (beg + end)
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid

        return end + k
