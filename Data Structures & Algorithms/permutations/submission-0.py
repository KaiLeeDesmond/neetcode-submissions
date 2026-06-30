class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        boo = [False]*len(nums)
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if boo[i] == True:
                    continue
                
                curr.append(nums[i])
                boo[i] = True
                dfs(curr)
                curr.pop()
                boo[i] = False
        dfs([])
        return res
        