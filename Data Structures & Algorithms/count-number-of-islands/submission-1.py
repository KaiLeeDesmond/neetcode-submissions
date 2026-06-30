class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0



        def bfs(r,c):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            q = collections.deque()

            q.append((r,c))
            visited.add((r,c))

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    x = dr+row
                    y = dc+col

                    if x in range(rows) and y in range(cols) and grid[x][y] == "1" and (x,y) not in visited:
                        visited.add((x,y))
                        q.append((x,y))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands

