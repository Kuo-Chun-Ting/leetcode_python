class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left, right = 0, 0
        window = set()

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_len = max(max_len, len(window))
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1

        return max_len
