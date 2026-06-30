class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ml = 0
        tes = set()
        for r in range(len(s)):
            while s[r] not in tes:
                tes.remove(s[l])
                l+=1
            tes.add(s[r])
            ml = max(ml,r-l+1)
        return ml
