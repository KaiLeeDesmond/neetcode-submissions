class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        tes = set(nums)
        for n in nums:
            if n-1 not in tes:
                continue
            length+=1
        return length
            

            