class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        use dfs
        base case is if we're already there
        i.e. if i == last index
        return true if so
        we need the end
        end can be the last index or the offset from the current index, i.e. i
        therefore, we need the min
        from there we need to iterate from i+1 to end + 1
        i+1 because we're checking from the 0th one initially
        then we loop and call dfs
        if dfs, return true
        else false
        '''

        def dfs(i):
            if i == len(nums) - 1:
                return True
            
            end = min (i+nums[i], len(nums)-1)
            for j in range(i+1,end+1):
                if dfs(j):
                    return True
            return False

        return dfs(0)
        