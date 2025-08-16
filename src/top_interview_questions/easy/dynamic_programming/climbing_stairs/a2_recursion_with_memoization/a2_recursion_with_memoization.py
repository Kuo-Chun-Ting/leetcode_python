class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0] * n
        return self.climb(0, n, mem)

    def climb(self, i: int, n: int, mem: list[int]) -> int:
        if i > n:
            return 0

        if i == n:
            return 1

        if mem[i] != 0:
            return mem[i]

        mem[i] = self.climb(i + 1, n, mem) + self.climb(i + 2, n, mem)
        return mem[i]
