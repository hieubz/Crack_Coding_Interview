from collections import Counter


class Solution:
    def repeatedNTimes(self, arr) -> int:
        dicts = {}
        for i in arr:
            if i not in dicts:
                dicts[i] = 1
            else:
                return i

    def repeatedNTimes_2(self, arr) -> int:
        count = Counter(arr)
        for k in count:
            if count[k] > 1:
                return k

    def repeatedNTimes_3(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i + k]:
                    return A[i]


s = Solution()
s.repeatedNTimes_3([1, 2, 3, 3])
