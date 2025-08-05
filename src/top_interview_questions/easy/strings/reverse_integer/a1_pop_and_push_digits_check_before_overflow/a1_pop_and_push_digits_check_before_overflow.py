class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x != 0:
            d = x % 10
            res = res * 10 + d

            if res > 2**31 - 1:
                return 0

            x = x // 10

        return res * sign
