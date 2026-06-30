class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self,node):
        curr = node
        while self.parent[curr] != curr:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]

        return curr
    
    def union(self,u,v):
        x = self.find(u)
        y = self.find(v)

        if x == y:
            return False
        if self.rank[y]>self.rank[x]:
            x,y=y,x
        self.rank[x]+=self.rank[y]
        self.parent[y] = x
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res-=1
        return res


                
        