class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        tes = set()

        for r in range(len(s)):
            while s[r] in tes:
                l+=1
                tes.remove(s[r])
            
            tes.add(s[r])
            longest = max(longest,r-l+1)
        
        return longest