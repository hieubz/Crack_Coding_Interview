import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned):
        words = re.findall(r'\w+', paragraph.lower())
        set_banned = set(banned)
        # count = Counter([w for w in words if w not in set_banned])

        dicts = {}
        remain_words = [w for w in words if w not in set_banned]
        for w in remain_words:
            if w not in dicts:
                dicts[w] = 1
            else:
                dicts[w] += 1

        max_count = 0
        result_word = ''
        for w, w_count in dicts.items():
            if w_count > max_count:
                max_count = w_count
                result_word = w

        return result_word

        # return count.most_common(1)[0][0]
