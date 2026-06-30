class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        tes = set()
        l = 0
        for r in range(len(s)):
            while s[r] in tes:
                tes.remove(s[l])
                l+=1
            tes.add(s[r])
            length = max(length,r-l+1)
        return length