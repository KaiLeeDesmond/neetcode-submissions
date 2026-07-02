class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')] +=1
            key = tuple(freq)
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]
            
        return list(hmap.values())

            
