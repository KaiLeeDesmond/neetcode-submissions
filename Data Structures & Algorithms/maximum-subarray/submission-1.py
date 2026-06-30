class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxx = nums[0]
        min_pref = 0
        x =0
        
        '''
        Input: nums = [2,-3,4,-2,2,1,-1,4]
        Input: inde = [0, 1,2, 3,4,5, 6,7]

        for 2 in nums:
            summ = 0 + 2 = 2
            a[2] = 2

        for -3 in nums:
            summ = 2-3 = -1
            a[-3] = -1
        '''

        for i in range(len(nums)):
            summ += nums[i]
            x = summ - min_pref
            maxx = max(x,maxx)
            min_pref = min(min_pref, summ)
        
        return maxx

        