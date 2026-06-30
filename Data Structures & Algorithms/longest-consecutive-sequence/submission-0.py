class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tes = set(nums)
        length = 0
        longest = 0

        for n in nums:
            if (n-1) not in tes:
                length = 0

                while (n+length) in tes:
                    length+=1
                
                longest = max(longest,length)
        return longest