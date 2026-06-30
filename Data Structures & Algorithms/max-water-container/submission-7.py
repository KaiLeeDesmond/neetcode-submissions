class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 1
        maxA=0
        area=0
        l = len(heights)-1
        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            maxA = max(maxA,area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxA
        