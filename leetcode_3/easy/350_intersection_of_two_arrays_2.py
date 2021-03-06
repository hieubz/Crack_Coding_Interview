class Solution:
    # sorted
    def intersect(self, nums1, nums2):
        dict_1 = {}
        for number in nums1:
            if number not in dict_1:
                dict_1[number] = 1
            else:
                dict_1[number] += 1

        inter_arr = []
        for number in nums2:
            if number in dict_1 and dict_1[number] > 0:
                dict_1[number] -= 1
                inter_arr.append(number)

        return inter_arr
