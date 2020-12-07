# class KthLargest:
#
#     def __init__(self, k, nums):
#         self.nums = sorted(nums, reverse=True)
#         self.k = k
#
#     def add(self, val):
#         location = self.binary_search(val)
#         self.nums.insert(location, val)
#         return self.nums[self.k - 1]
#
#     def binary_search(self, val):
#         l, r = 0, len(self.nums) - 1
#
#         while l <= r:
#             mid = (l + r) // 2
#             if self.nums[mid] == val:
#                 return mid
#             elif self.nums[mid] > val:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#
#         return l
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
