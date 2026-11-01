class Solution:
    def countOddDigit(self, n):
        odd = 0
        while n >0:
            last = n %10
            if last % 2 != 0:
                odd +=1
            n = n//10
        return odd
