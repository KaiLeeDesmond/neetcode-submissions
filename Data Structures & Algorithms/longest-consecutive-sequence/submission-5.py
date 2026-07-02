class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        count = 1
        tes = set(nums)
        for n in nums:
            x = n
            if x-1 not in tes:
                while x+1 in tes:
                    count+=1
                    x+=1
            length = max(length,count)
            count = 0
        return length
            

            