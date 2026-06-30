class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        first we need to check if the index iself is reachable 
        that's why we compare i with farthest
        then we maximize the nums[i] + i with the farthest

        then we return true
        '''

        farthest = 0

        for i in range(len(nums)):
            if i>farthest:
                return False
            farthest = max(nums[i]+i,farthest)
        return True