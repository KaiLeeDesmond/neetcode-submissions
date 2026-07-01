class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for x in range(len(nums)):
            hmap[nums[x]] = x

        for n in nums:
            diff = target - n
            if diff in hmap and hmap[diff] != n:
                return [hmap[n],hmap[diff]]
        return []
