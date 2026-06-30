class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        first check if the length of the strings are the same
        if not, return false

        then make a hash map where the keys are the characters of 
        the first string and the values are the associated count 
        of the characters

        then, loop through the second string, and whenever the 
        characters are matching, reduce the count of each matched
        char by 1

        if the values in the hash map are 0, it's true
        else it's false 
        '''
        hmap = {}
        if len(s) != len(t):
            return False
        
        for c in s:
            hmap[c] = hmap.get(c,0) + 1
        
        for c in t:
            if c not in hmap or hmap[c] == 0:
                return False
            hmap[c] -= 1
        for val in hmap.values():
            if val != 0:
                return False
        return True


        