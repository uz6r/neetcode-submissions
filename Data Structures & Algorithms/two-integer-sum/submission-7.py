class Solution:
    def twoSum(self, nums, target):
        seen = {}  # hashmap to store: number -> index we've seen before
        for i, n in enumerate(nums):  # loop through array with index + value
            needed = target - n  # the number we need to complete the target
            if needed in seen:  # have we seen the complement before?
                return [seen[needed], i]  
                # yes → return index of complement + current index
            seen[n] = i  
            # no → store current number with its index for future checks
        return []