class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cs =0
        diff = 0
        hmap = {0:1}
        res = 0

        for n in nums:
            cs+=n
            diff = cs-k
            res += hmap.get(diff,0)
            hmap[cs] = hmap.get(cs,0)+1
        return res