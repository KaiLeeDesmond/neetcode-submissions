class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(speed) -> bool:
            return sum(math.ceil(pile/speed) for pile in piles) <= h
        
        l = 1
        r = max(piles)

        while l<r:
            mid = l + (r-l)//2
            if helper(mid):
                r = mid
            else:
                l = mid+1
        return l 