class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if len(nums) - 1 == i:
                return True
            
            if i in memo:
                return memo[i]
            
            end = min(nums[i]+i, len(nums)-1)

            for j in range(i+1,end+1):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)

