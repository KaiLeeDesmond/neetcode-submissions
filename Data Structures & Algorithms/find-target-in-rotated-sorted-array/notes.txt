class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or nums[l] > target: #if target is outside the left array, move the left pointer
                    l = m+1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target<nums[m]: #if target is outside the right subarray, move the right pointer
                    r = m - 1
                else:
                    l = m + 1
        return -1
