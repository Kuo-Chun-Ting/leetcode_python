class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_alpha_count: dict[str, int] = {}
        t_alpha_count: dict[str, int] = {}

        for c in s:
            if c not in s_alpha_count:
                s_alpha_count[c] = 1
            else:
                s_alpha_count[c] += 1

        for c in t:
            if c not in t_alpha_count:
                t_alpha_count[c] = 1
            else:
                t_alpha_count[c] += 1

        if len(s_alpha_count) != len(t_alpha_count):
            return False

        for k, v in s_alpha_count.items():
            if k not in t_alpha_count or t_alpha_count[k] != v:
                return False

        return True
