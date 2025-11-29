class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left, right = 0, 0
        window: dict = {}

        while right < len(s):
            c = s[right]
            if c in window and window[c] >= left:
                left = window[c] + 1

            window[c] = right
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
