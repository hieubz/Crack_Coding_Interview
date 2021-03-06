import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned):
        words = re.findall(r'\w+', paragraph.lower())
        # words = re.sub(r'[^a-zA-Z]', ' ', paragraph).split()
        banned = set(banned)

        return Counter([w for w in words if w not in banned]).most_common(1)[0][0]
