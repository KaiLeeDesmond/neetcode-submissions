class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        pref = [0]*len(nums)
        res = [0]*len(nums)
        for i in range(len(nums)-1):
            pref[i] = nums[i+1] * nums[i]
        
        for i in range(len(nums)-2,-1,-1):
            suff[i] = nums[i-1]*nums[i]
        
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]

        return res
        