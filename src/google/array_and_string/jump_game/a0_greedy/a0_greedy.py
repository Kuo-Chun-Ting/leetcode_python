# Greedy from left to right
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        farest_idx = 0
        for i in range(n):
            if farest_idx < i:
                return False

            steps = nums[i]
            farest_idx = max(farest_idx, i + steps)
            if farest_idx >= n - 1:
                return True

        return True
