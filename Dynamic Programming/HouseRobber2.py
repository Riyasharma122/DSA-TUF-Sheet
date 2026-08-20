class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_linear(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            return dp[n - 1]
        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])
        return max(case1, case2)


    
    class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(arr):
            n = len(arr)
            dp = [-1] * n

            def solve(i):
                if i < 0:
                    return 0

                if i == 0:
                    return arr[0]

                if dp[i] != -1:
                    return dp[i]

                dp[i] = max(
                    solve(i - 1),
                    arr[i] + solve(i - 2)
                )

                return dp[i]

            return solve(n - 1)

        # Don't rob the last house
        case1 = rob_linear(nums[:-1])

        # Don't rob the first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)