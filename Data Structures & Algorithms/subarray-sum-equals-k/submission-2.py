class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        cs = 0
        diff = 0
        res = 0

        for num in nums:
            cs +=num

            diff = cs-k

            res += hmap.get(diff,0)
            hmap[cs] = 1 + hmap.get(cs,0)
        return res
        
        