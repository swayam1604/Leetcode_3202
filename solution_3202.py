class Solution:
    def maximumLength(self, nums, k):
        n = len(nums)
        from collections import defaultdict

        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1 if mod in dp[j] else 2)
                max_len = max(max_len, dp[i][mod])

        return max_len
