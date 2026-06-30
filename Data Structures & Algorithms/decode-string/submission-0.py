class Solution:
    def decodeString(self, s: str) -> str:
        ss = []
        cs = []
        k = 0
        curr = ""
        temp = ""

        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            
            elif c == "[":
                ss.append(curr)
                cs.append(k)
                k = 0
                curr = ""
            
            elif c == "]":
                temp = curr
                curr = ss.pop()
                count = cs.pop()
                curr = curr + (temp*count)
            else:
                curr += c

        return curr


        