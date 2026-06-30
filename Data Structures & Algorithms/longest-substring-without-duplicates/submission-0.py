class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        first we need a l and an r
        we also need a set since it's non repeating chars
        algo:

        traverse the string

        check if char's in the set
        if yes, then 'pop' from set and advance l
        else, add to set
        update res = max(res,r-l+1) --> r-l+1 helps us track number of chars
        '''
        l = 0
        res = 0
        r = 0
        tes = set()

        for r in range(len(s)):
            while s[r] in tes:
                tes.remove(s[l])
                l+=1
            tes.add(s[r])
            res = max(res,r-l+1)
        return res
                