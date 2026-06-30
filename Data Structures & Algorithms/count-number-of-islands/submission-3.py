class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        islands = 0
        def dfs(r,c):
            if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0:
                return
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands+=1
                    dfs(r,c)

        return islands

        