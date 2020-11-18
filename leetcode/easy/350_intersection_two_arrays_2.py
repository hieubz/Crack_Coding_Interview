# given two arrays, write a function to compute their intersection
from collections import Counter


class Solution:

    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        return list((c1 & c2).elements())

    def intersect_2(self, nums1, nums2):
        pass