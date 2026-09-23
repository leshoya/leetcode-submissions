from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        counts = Counter(s)
        for key in counts:
            if counts[key] == 1:
                return s.index(key)
        return -1