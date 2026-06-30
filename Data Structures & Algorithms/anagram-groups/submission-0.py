class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            char_count_array = [0,]*26
            for c in string:
                char_count_array[ord(c) - ord('a')] +=1
            res[tuple(char_count_array)].append(string)
        return list(res.values())


        