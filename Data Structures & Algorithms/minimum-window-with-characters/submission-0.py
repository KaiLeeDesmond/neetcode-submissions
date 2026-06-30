class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap = {}
        minl = 999
        l = 0
        formed = 0
        start = 0

        for c in t:
            hmap[c] = hmap.get(c,0) + 1

        required = len(hmap)
        
        for r in range(len(s)):
            if s[r] in hmap:
                hmap[s[r]] = hmap.get(s[r],0) - 1
            if s[r] in hmap and hmap[s[r]] == 0:
                formed += 1

            while formed == required:
                if r-l+1 < minl:
                    minl = r-l+1
                    start = l
                if s[l] in hmap and hmap[s[l]] == 0:
                    formed -= 1
                if s[l] in hmap:
                    hmap[s[l]] +=1
                l+=1
        return "" if minl == 999 else s[start:start+minl]


