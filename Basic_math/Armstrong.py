class Solution:
    def isArmstrong(self, n):
        original = n
        digits = len(str(n))
        total = 0
        while n > 0:
            last = n % 10
            total += last ** digits
            n //= 10
        return total == original