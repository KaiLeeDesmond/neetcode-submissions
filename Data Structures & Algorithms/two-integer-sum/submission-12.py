class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for x in range(len(nums)):
            hmap[nums[x]] = x

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hmap and hmap[diff] != i:
                return [i,hmap[diff]]
        return []
