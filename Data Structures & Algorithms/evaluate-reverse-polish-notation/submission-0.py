class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = ["x"]*len(tokens)
        tos = -1
        for t in tokens:
            if ord('0') - ord(t) in range(48,58):
                stack[tos+1] = t
            
            else:
                c = 0
                while not stack:
                    a = stack[-1]
                    b = stack[-2]
                    

                    if t == "*":
                        c = a*b
                    elif t == "+":
                        c = a+b
                    elif t == "-":
                        c = a-b
                    else:
                        c = a/b
                stack[tos+1] = c

            
        