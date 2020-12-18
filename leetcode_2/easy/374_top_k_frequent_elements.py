from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        dicts = {}
        for num in nums:
            if num not in dicts:
                dicts[num] = 1
            else:
                dicts[num] += 1

        dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)

        return [ele[0] for ele in dicts[:k]]
