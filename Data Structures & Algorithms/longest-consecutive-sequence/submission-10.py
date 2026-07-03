class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tes = set(nums)
        count = 0
        length = 0
        for n in nums:
            x = n
            if n-1 not in tes:
                count = 1
                while x+1 in tes:
                    count+=1
                    x+=1
                length = max(length,count)
        return length

