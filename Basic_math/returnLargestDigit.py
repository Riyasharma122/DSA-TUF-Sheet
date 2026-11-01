class Solution:
    def largestDigit(self, n):
        prev = 0
        while n >0:
            rem = n %10
            if prev<= rem:
                prev = rem
            n = n //10
        return prev
