class Solution:
    def divisors(self, n):
        arr = []
        for j in range(1,n+1):
            if n%j==0:
                arr.append(j)
        return arr