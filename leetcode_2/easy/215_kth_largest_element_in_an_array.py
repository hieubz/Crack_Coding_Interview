import random


class Solution:
    def find_second_largest(self, nums):
        max_1, max_2 = 0, 0
        for num in nums:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2 and num != max_1:
                max_2 = num

        return max_2

    def find_kth_largest_element_2(self, nums, k):
        nums = sorted(nums, reverse=True)
        return nums[k - 1]

    def find_kth_largest_element(self, nums, k):
        if not nums:
            return
        p = random.choice(nums)
        l, m, r = [x for x in nums if x > p], [x for x in nums if x == p], [x for x in nums if x < p]

        nums, i, j = l + m + r, len(l), len(l) + len(m)
        if k <= i:
            return self.find_kth_largest_element(nums[:i], k)
        elif k > j:
            return self.find_kth_largest_element(nums[j:], k - j)
        else:
            return nums[i]


s = Solution()
print(s.find_second_largest([1, 3, 2, 16, 3, 7, 9]))
