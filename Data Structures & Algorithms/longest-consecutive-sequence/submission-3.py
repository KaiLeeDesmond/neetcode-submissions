class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tes = set(nums)
        longest = 0
        maxL = 0
        length = 0
        for n in nums:
            if n-1 not in tes:
                length = 0
            
            while n+length in tes:
                length+=1
            
            maxL = max(maxL,length)
        
        return maxL

