class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]
        def solve(i, prev):
            if i == n:
                return 0
            if dp[i][prev + 1] != -1:
                return dp[i][prev + 1]
            not_take = solve(i + 1, prev)
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + solve(i + 1, i)
            dp[i][prev + 1] = max(take, not_take)
            return dp[i][prev + 1]
        return solve(0, -1)

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)