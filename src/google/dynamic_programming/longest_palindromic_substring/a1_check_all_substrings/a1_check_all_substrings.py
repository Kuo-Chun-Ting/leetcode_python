class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        for length in range(n, 0, -1):
            for j in range(0, n - length + 1):
                substr = s[j : j + length]

                if self.is_palindrome(substr):
                    return substr

        return ""

    def is_palindrome(self, s) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
