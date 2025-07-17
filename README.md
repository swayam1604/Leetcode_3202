# 🚀 LeetCode 3202 – Find the Maximum Length of Valid Subsequence II

## 🧩 Problem Statement

You are given an integer array `nums` and a positive integer `k`.

A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:
(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k


Return the length of the **longest valid subsequence** of `nums`.

---

## ✅ Examples

### Example 1:
**Input:**  
`nums = [1, 2, 3, 4, 5]`, `k = 2`  
**Output:**  
`5`  
**Explanation:**  
The entire array is valid. All adjacent sums modulo 2 are equal.

### Example 2:
**Input:**  
`nums = [1, 4, 2, 3, 1, 4]`, `k = 3`  
**Output:**  
`4`  
**Explanation:**  
A valid subsequence is `[1, 4, 1, 4]`, with all adjacent sums ≡ 2 (mod 3)

---

## 🧠 Approach

We use **Dynamic Programming** to keep track of the longest valid subsequence ending at each index `i`, where all adjacent sums `(a + b) % k` are equal.

### Key Ideas:
- For each pair `(nums[j], nums[i])` where `j < i`, compute `mod = (nums[j] + nums[i]) % k`
- Use `dp[i][mod]` to represent the longest valid subsequence ending at index `i` with adjacent sum modulo `mod`
- Update `dp[i][mod]` as:
  - `dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)` if `dp[j][mod]` exists
  - Else, initialize with length `2` (starting new pair)
- Track global `max_len` as the result

---

## ✅ Python Code

```python
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

- Complexity
Time: O(n²)
Space: O(n·k)
Efficient for n <= 1000 and k <= 1000 as per problem constraints.

Developed with 💻 by Swayam Sharma

