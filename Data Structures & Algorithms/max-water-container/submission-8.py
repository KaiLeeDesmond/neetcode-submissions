class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        maxA=0
        area=0
        r = len(heights)-1
        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            maxA = max(maxA,area)

            if heights[l]<heights[r]:
                l+=1
            else: #this else is for when l and r overlap, or have the same height
                r-=1
            
        return maxA
        