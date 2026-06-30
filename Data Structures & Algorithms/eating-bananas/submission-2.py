class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(speed) -> bool:
            return sum ((pile-1)//speed+1 for pile in piles) <= h
        
        l = 1
        r = max(piles)
        mid = 0

        while l<r:
            mid = l + (r-l)//2
            if helper(mid):
                r = mid
            else:
                l = mid+1
        return l
        