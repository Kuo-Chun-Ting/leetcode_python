class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left, right = 0, 0
        seen: dict[str, int] = {}

        for i, c in enumerate(s):
            while c in seen and seen[c] >= left:
                left += 1

            seen[c] = i
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
