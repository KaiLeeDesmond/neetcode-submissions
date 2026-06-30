class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                if t == "+":
                    res = int(stack.pop()) + int(stack.pop())
                elif t == "-":
                    a,b = stack.pop(),stack.pop()
                    res = int(b)-int(a)
                elif t == "*":
                    res = int(stack.pop()) * int(stack.pop())
                else:
                    a,b = stack.pop(),stack.pop()
                    res = float(int(b)//int(a))
                stack.append(res)
            else:
                stack.append(t)
        return stack[0]
                

        