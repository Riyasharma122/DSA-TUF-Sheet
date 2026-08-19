class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        n = len(nums)
        for i in range(0,n):
            if(nums[i]>largest):
                largest = nums[i]
        return largest       