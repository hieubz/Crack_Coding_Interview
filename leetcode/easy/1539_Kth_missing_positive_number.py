class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        dicts = {}
        for num in arr:
            dicts[num] = 1

        count = 0
        for i in range(1, arr[-1] + k + 1):
            if i not in dicts:
                count += 1
                if count == k:
                    return i

    def findKthPositive_2(self, arr, k):
        l, r = 0, len(arr)

        while l < r:
            m = (l + r) // 2
            # count space
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k


s = Solution()
s.findKthPositive_2([2, 3, 4, 7, 11], 5)

