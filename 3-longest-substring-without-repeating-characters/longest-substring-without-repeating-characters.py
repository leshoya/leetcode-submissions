class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        map = dict() #value: index last seen
        left = 0
        #abca
        # l = 3
        #{ a: 0, b:1, c:2}
        for r, c in enumerate(s):
            if c in map:
                left = max(left, map[c] + 1)
            map[c] = r
            longest = max(longest, r - left + 1)
        return longest


        