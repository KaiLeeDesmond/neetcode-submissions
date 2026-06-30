class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        if len(s) != len(t):
            return False
        for c in s:
            hmap[c] = hmap.get(c,0)+1

        for c in t:
            if c not in hmap or hmap[c] == 0:
                return False
            hmap[c] -=1

        for val in hmap.values():
            if val !=0:
                return False
        return True

        