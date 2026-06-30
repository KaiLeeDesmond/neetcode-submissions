class Solution:
    def reverse(self, x: int) -> int:
        n = x
        rev = 0
        y = 0
        flag = False


        if x < 0:
            n = -x
            flag = True

        while n>0:
            y = n%10
            rev = rev*10 + y
            n = n//10

        if rev > ((2**31) - 1) or rev < -1 * (2**31):
            return 0
        
        if flag and rev == x:
            return -rev

        return rev

        
        