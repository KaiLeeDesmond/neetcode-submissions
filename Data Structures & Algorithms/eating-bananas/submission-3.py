class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(speed) -> bool :
            return sum ((pile-1)//speed+1 for pile in piles) <= h
        
        l = 1
        r = max(piles)

        while l<r:
            mid = l + (r-l) // 2

            if helper(mid):
                r = mid #this one might be the answer, so we need to 
                        # store it and check for more
            else:
                l = mid+1
                    #this one is too slow, therefore we have to check the next one
        return l
