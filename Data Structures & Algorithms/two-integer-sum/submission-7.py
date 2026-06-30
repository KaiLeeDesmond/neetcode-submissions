class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,a in enumerate(nums):
            diff = target - a
            if diff in hmap:
                return [hmap[diff],i]
            
            hmap[a] = i
        
        # return []