class Solution:
    def reverseNumber(self, n):
        new = 0
        while n >0:
            last = n %10
            new = (new *10) + last
            n //=10
        return new