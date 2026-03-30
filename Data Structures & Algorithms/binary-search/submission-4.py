class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # define search boundaries
        while l <= r:  # continue while there is a valid search space
            mid = (l + r) // 2  # get middle index
            if nums[mid] == target:
                return mid  # target found, return index
            elif nums[mid] < target:
                # middle value too small → discard left half (including mid)
                l = mid + 1
            else:
                # middle value too large → discard right half (including mid)
                r = mid - 1
        return -1  # target not found