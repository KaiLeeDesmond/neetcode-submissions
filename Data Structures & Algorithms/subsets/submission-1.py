class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(temp,start):
            res.append(temp[:])

            for i in range(start,len(nums)):
                temp.append(nums[i])
                dfs(temp,i+1)
                temp.pop()
        
        dfs([],0)
        return res
                