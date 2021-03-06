import random


class Solution:
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)

        left = []
        mid = []
        right = []
        for number in nums:
            if number > pivot:
                left.append(number)
            elif number < pivot:
                right.append(number)
            else:
                mid.append(number)

        l, m = len(left), len(mid)

        if k <= l:
            return self.findKthLargest(left, k)
        elif k > l + m:
            return self.findKthLargest(right, k - l - m)
        else:
            return mid[0]


s = Solution()
a = s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(a)
