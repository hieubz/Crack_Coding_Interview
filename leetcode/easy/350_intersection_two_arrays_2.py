# given two arrays, write a function to compute their intersection
# follow up
# 1. what if the given array is already sorted? How would you optimize your algorithm
# 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 3. what if elements of nums2 are stored on disk, and the memory is limited such that you cannot
# load all elements into the memory at once?


# Answers:
# 2: suppose lengths of two arrays are N and M, the time complexity of second solution is O(M + N) and
# the space complexity if O(N) considering the hash. So it's better to use the smaller array to
# construct the hash table (dict)

# 3. If only nums2 cannot fit in memory, put all elements of nums1 into a Hashmap, I would read chunks of array
# that fit into the memory, and record the intersections
# If both arrays cannot fit in memory => use distributed system, maybe MapReduce to solve.


from collections import Counter


class Solution:

    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        return list((c1 & c2).elements())

    def intersect_2(self, nums1, nums2):
        dicts = {}
        for i in nums1:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1

        result = []

        for i in nums2:
            if i in dicts and dicts.get(i) > 0:
                result.append(i)
                dicts[i] -= 1

        return result

    # follow up 1: sorted array
    # => use two pointer iteration, i points to nums1 and j points to nums2
    # because a sorted array is in ascending order, so if nums1[i] > nums2[j]
    # , we need to increment j, and vice versa. Only when nums1[i] == nums2[j]
    # we add it to the result array. Time Complexity is O(max (M, N))
    def intersection_3(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        len1 = len(nums1)
        len2 = len(nums2)

        i, j = 0, 0
        result = []
        while i < len1 and j < len2:
            a = nums1[i]
            b = nums2[j]
            if a == b:
                result.append(a)
            elif a < b:
                i += 1
            else:
                j += 1

        return result
