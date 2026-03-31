class Solution:
    def firstUniqChar(self, s: str) -> int:
        # frequency map for lowercase letters
        count = {}

        # first pass: count occurrences
        for c in s:
            count[c] = count.get(c, 0) + 1

        # second pass: find first character with count == 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i  # index of first unique character

        return -1  # no unique character found