class Solution:
    def LCM(self, n1, n2):
        num = max(n1, n2)
        while True:
            if num % n1 == 0 and num % n2 == 0:
                return num
            num += 1

# import math
#return math.lcm(n1,n2)