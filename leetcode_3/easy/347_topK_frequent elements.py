from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        dicts = {}
        for number in nums:
            if number not in dicts:
                dicts[number] = 1
            else:
                dicts[number] += 1

        dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)  # O(nlogn)
        return [ele[0] for ele in dicts[:k]]

    def top2(self, nums, k):
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z, v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)

        arr = []

        for x in range(len(nums), 0, -1):
            if x in frq:
                arr.extend(frq[x])
            if len(arr) >= k:
                return arr[:k]

        return arr[:k]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    result = s.top2(nums, 2)
    print(result)