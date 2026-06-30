class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1


# 10 20 30 40 50
# 0  1  2  3  4

# mid = 0+4//2 = 2
# target = 20

# a[mid] > target
# 30 > 20? Yes
