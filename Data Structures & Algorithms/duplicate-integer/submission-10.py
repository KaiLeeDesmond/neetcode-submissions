class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return set(nums)>len(nums)