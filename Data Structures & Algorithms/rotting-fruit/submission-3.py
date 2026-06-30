class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh>0 and q:
            length = len(q)

            for i in range(length):
                r,c = q.popleft()

                for dr,dc in directions:
                    x = dr+r
                    y = dc+c
                    if x in range(rows) and y in range(cols) and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x,y))
                        fresh-=1
            time +=1
        
        return time if fresh ==0 else -1