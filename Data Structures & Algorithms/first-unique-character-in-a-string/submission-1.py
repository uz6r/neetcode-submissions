class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            if c.isalpha():
                count[c] = count.get(c, 0) + 1
        for i, c in enumerate(s):
            if c.isalpha() and count[c] == 1:
                return i
        return -1