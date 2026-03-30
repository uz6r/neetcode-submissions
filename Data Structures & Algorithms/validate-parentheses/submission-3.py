class Solution:
    def isValid(self, s: str) -> bool:

        # ==============================
        # APPROACH 1: NO MAPPING (ALT)
        # ==============================
        # stack = []  # stack to track opening brackets
        #
        # for c in s:
        #     # if it's an opening bracket, push to stack
        #     if c in '([{':
        #         stack.append(c)
        #     else:
        #         # it's a closing bracket
        #
        #         # if stack is empty, nothing to match → invalid
        #         if not stack:
        #             return False
        #
        #         top = stack.pop()  # get last opening bracket
        #
        #         # check if the bracket types match
        #         if c == ')' and top != '(':
        #             return False
        #         if c == ']' and top != '[':
        #             return False
        #         if c == '}' and top != '{':
        #             return False
        #
        # # valid only if no unmatched opening brackets remain
        # return len(stack) == 0


        # ==============================
        # APPROACH 2: WITH MAPPING (USED)
        # ==============================
        stack = []  # stack to track opening brackets
        mapping = {')': '(', ']': '[', '}': '{'}  # closing → opening

        for c in s:
            if c in mapping:
                # closing bracket: check match
                if not stack:
                    return False
                top = stack.pop()
                if mapping[c] != top:
                    return False
            else:
                # opening bracket: push
                stack.append(c)

        # valid only if no unmatched opening brackets remain
        return len(stack) == 0