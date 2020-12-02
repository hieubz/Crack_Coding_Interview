from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dicts = {}
        for i in arr:
            dicts[i] = dicts.get(i, 0) + 1

        num_occurs = list(dicts.values())
        if len(set(num_occurs)) != len(num_occurs):
            return False
        else:
            return True

    def uniqueOccurrences_2(self, arr) -> bool:
        c = Counter(arr)

        return len(c) == len(set(c.values()))
