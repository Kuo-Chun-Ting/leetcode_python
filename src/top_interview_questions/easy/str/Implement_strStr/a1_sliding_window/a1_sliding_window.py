class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        i = 0
        while i <= len(haystack) - len(needle):
            while i < len(haystack) and haystack[i] != needle[0]:
                i += 1

            if i == len(haystack):
                return -1

            start_idx = i
            j = 0

            while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == len(needle):
                return start_idx

            i = start_idx + 1

        return -1
