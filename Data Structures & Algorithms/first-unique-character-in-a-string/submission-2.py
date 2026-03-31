class Solution:
    def firstUniqChar(self, s: str) -> int:
        # frequency map to count occurrences of each character
        count = {}

        # first pass: build frequency map
        # only counting alphabetic characters (ignores digits/symbols)
        for c in s:
            if c.isalpha():
                count[c] = count.get(c, 0) + 1

        # second pass: find first character with frequency == 1
        # preserves original order by iterating over string again
        for i, c in enumerate(s):
            if c.isalpha() and count[c] == 1:
                return i  # return index of first unique character

        # no unique alphabetic character found
        return -1