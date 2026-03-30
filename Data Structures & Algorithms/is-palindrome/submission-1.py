class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # two pointers from both ends

        while l < r:
            # move left pointer until it points to an alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            
            # move right pointer until it points to an alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1
            
            # compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False  # mismatch → not a palindrome
            
            # move both pointers inward
            l += 1
            r -= 1
        
        # if all characters matched, it's a palindrome
        return True