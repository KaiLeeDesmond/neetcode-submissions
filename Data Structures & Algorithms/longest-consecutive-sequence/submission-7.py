class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tes = set(nums)
        count = 1
        x = 0
        length = 1
        for n in nums:
            if n-1 not in tes:
                x = n
                count = 1
                while x+1 in tes:
                    count+=1
                    x+=1
                length = max(length,count)
                count = 1
        return length

