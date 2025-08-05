class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if any(len(s) == 0 for s in strs):
            return ""

        min_len = min(len(s) for s in strs)

        i = 0
        while i < min_len:
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return strs[0][:i]

            i += 1

        return strs[0][:i]
