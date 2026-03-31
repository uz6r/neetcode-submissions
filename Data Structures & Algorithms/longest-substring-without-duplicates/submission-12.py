class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # stores characters in current window
        l = 0  # left pointer of window
        max_len = 0  # track maximum length found

        for r in range(len(s)):  # expand window with right pointer
            # if duplicate character found, shrink window from left
            # keep removing until s[r] is no longer in the set
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])  # add current character to window

            # update maximum length of valid window
            # (r - l + 1) gives current window size
            max_len = max(max_len, r - l + 1)
        
        return max_len  # return longest substring length