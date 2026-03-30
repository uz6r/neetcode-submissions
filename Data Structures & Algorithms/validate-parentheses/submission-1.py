class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[c] != top:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
                