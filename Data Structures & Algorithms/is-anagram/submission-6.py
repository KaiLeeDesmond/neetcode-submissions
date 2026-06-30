class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap = {}

        for c in s:
            hmap[c] = hmap.get(c,0) + 1

        for c in t:
            if c not in hmap or hmap[c] == 0:
                return False
            hmap[c] -=1
            
        
        for i in hmap.keys():
            if hmap[i] != 0:
                return False
        return True


        