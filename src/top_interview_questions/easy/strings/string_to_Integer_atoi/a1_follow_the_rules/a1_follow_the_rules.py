class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0
        MAX = 2**31 - 1
        MIN = -(2**31)

        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            sign = 1
            i += 1

        while i < len(s):
            if not s[i].isdigit():
                break

            res = 10 * res + int(s[i])

            if res * sign > MAX:
                return MAX
            if res * sign < MIN:
                return MIN

            i += 1

        return res * sign
