class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        # for c in s:
        #     hmap[c] = hmap.get(c,0) + 1
        l = 0 
        max_len= 0
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r],0) + 1
            while (r-l+1) - max(hmap.values()) > k:
                hmap[s[l]]-=1
            max_len = max(max_len,r-l+1)
        
        return max_len

            