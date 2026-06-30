class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        first iterate through the strings
        then make an empty frequency array
        then iterate through the chars
        update the frequency array based on the char
        add to result
        return result
        '''
        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - 97]+=1
            res[tuple(count)].append(s)
        
        return list(res.values())