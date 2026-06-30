class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tes = set()
        l = 0
        r =0
        length = 0

        for r in range(len(s)):
            while s[r] in tes:
                tes.remove(s[l])
                l+=1
            
            tes.add(s[r])
            length = max(length, r-l+1)
        return length
        