class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0]*len(nums)
        summ = 0
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

        for i in range(len(nums)+1):
            summ += nums[i]
            a[i] = summ
        
        a.sort()
        return a[-1]

        