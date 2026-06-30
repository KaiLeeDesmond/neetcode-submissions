class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in nums:
            if i >= farthest:
                return False
            farthest = max(nums[i] + i, farthest)
        return True
        