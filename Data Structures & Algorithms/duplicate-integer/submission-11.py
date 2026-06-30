class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if set(nums)<len(nums):
            return True
        return False