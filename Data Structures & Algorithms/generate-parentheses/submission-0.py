class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(op, c):

            if op == c == n:
                res.append("".join(stack))
                return
            
            if op < n:
                stack.append("(")
                backtrack(op+1,c)
                stack.pop()
            
            if c < op:
                stack.append(")")
                backtrack(op,c+1)
                stack.pop()
        
        backtrack(0,0)
        return res


