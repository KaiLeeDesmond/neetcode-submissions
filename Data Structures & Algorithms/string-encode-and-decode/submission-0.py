class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            # 4#hello
            x+=len(s)+"#"+s
        return x

    def decode(self, s: str) -> List[str]:
        word = ""
        res = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            length= int(s[i:j])

            word = s[j+1:j+1+length]

            res.append(word)

            i = 1+j+length
        
        return res

