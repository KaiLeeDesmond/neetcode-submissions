class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def fed(speed) -> bool:
            return sum((pile-1)//speed+1 for pile in piles) <= h
        
        l,r = 0,max(piles)

        while l<r:
            mid = l+ (r-l)//2

            if fed(mid):
                r = mid
            else:
                l = mid+1
        return l

        