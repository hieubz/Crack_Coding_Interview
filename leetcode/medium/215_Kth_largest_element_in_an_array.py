# find the Kth largest element in an unsorted array.
import random


class Solution:
    # O(NlogN) running time and O(1) memory
    def findKthLargest(self, nums, k: int):
        nums = sorted(nums, reverse=True)
        return nums[k - 1]

    def findKthLargest_2(self, nums, k: int):
        if not nums:
            return
        # find a random pivot
        p = random.choice(nums)
        # use 2 pointers l, r, divide and conquer
        # we dont need to sort all the array
        l, m, r = [x for x in nums if x > p], [x for x in nums if x == p], [x for x in nums if x < p]
        nums, i, j = l + m + r, len(l), len(l) + len(m)

        # conquer
        return self.findKthLargest_2(nums[:i], k) if k <= i else self.findKthLargest_2(nums[j:], k - j) if k > j else \
        nums[i]


s = Solution()
res = s.findKthLargest_2([3, 2, 1, 5, 6, 4], 3)
print(res)
