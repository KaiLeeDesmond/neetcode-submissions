class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tes = set()
        res = 0
        l=0

        for r in range(len(s)):
            while s[r] in tes:
                tes.remove(s[r])
                l+=1
            
            tes.add(s[r])
            res = max(res,r-l+1)
        
        return res
        