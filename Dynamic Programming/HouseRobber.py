class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]
class Solution:
    def rob(self, nums):
        n = len(nums)

        dp = [-1] * n

        def solve(i):
            # Base cases
            if i == 0:
                return nums[0]

            if i < 0:
                return 0

            # Already calculated
            if dp[i] != -1:
                return dp[i]

            dp[i]= max(solve(i-1),num[i]+ solve(n-2))
            return dp[i]

        return solve(n - 1)