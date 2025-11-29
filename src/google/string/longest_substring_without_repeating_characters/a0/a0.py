class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = []
        curr_subsctring = []

        for c in s:
            if c in curr_subsctring:
                max_substring = (
                    curr_subsctring
                    if len(curr_subsctring) > len(max_substring)
                    else max_substring
                )
                idx = None
                for i, sc in enumerate(curr_subsctring):
                    if sc == c:
                        idx = i
                curr_subsctring = curr_subsctring[idx + 1 :] + [c]
            else:
                curr_subsctring.append(c)

        max_substring = (
            curr_subsctring
            if len(curr_subsctring) > len(max_substring)
            else max_substring
        )
        return len(max_substring)
