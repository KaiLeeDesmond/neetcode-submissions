class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        hmap = {}

        for i,num in enumerate(nums):
            diff = target-num
            if diff in hmap:
                return [hmap[diff],i]
            hmap[num] = i
        return []
        