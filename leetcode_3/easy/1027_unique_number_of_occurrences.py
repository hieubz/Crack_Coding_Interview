from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dict = {}
        for number in arr:
            if number not in dict:
                dict[number] = 1
            else:
                dict[number] += 1

        occur_counts = dict.values()
        s = set()
        for count in occur_counts:
            if count not in s:
                s.add(count)
            else:
                return False

        return True
