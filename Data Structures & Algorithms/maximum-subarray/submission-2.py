class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxx = nums[0]
        min_pref = 0
        x =0
        
        '''
        Input: nums = [2,-3,4,-2,2,1,-1,4]
        Input: inde = [0, 1,2, 3,4,5, 6,7]
        '''

        for i in range(len(nums)):
            summ += nums[i]
            x = summ - min_pref #kadane's line here
            maxx = max(x,maxx)
            min_pref = min(min_pref, summ)
        
        return maxx

        