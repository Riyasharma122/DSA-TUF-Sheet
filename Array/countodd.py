class Solution:
    def countOdd(self, arr, n):
        count= 0
        for num in arr:
            if(num % 2!=0):
                count+= 1
        return count
