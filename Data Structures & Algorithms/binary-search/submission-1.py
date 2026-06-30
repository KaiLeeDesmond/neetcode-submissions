class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0
        r = len(nums)-1
        if target not in nums:
            return -1
        while l<r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                r = mid
            else:
                l = mid+1
            return l
        return -1
    