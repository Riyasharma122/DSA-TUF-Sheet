class Solution:
    def isPalindrome(self, n):
        num = n
        new= 0
        while n >0:
            last = n %10
            new = (new *10)+last
            n//=10
        return new== num

