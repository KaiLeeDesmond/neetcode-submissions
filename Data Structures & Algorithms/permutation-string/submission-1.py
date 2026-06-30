class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hmap = {}
        for c in s1:
            hmap[c] = 1 + hmap.get(c,0)

        l = 0
        for r in range(len(s2)):
            hmap[s2[r]] = hmap.get(s2[r],0) - 1

            if (r-l+1) > len(s1):
                hmap[s2[l]]+=1
                l+=1
            
            if (r-l+1) == len(s1):
                if all(v == 0 for v in hmap.values()):
                    return True 
        return False

        