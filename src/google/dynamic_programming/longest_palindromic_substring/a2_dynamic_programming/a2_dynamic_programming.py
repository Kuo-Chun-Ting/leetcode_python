class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        largest_len = 1
        start_idx = 0
        dp: list[list[int]] = [[False] * n for _ in range(n)]

        # Setup length 1
        for i in range(n):
            dp[i][i] = True

        # Setup length 2
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                start_idx = i
                largest_len = 2

        # Setup length remaining
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    largest_len = length
                    start_idx = i

        return s[start_idx : start_idx + largest_len]
