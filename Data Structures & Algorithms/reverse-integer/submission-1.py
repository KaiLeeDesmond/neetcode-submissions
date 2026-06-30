class Solution:
    def reverse(self, x: int) -> int:
        n = -x if x<0 else x
        rev = 0
        y = 0

        while n>0:
            y = n%10
            rev = rev*10 + y
            n = n//10

        if rev > ((2**31) - 1) or rev < -1 * (2**31):
            return 0
        
        if x<0:
            return -rev

        else:
            return rev

        return 0

        
        