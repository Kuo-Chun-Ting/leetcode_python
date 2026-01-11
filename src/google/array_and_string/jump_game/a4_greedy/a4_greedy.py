class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        last_good_idx = n - 1

        for i in range(n - 2, -1, -1):
            steps = nums[i]
            if i + steps >= last_good_idx:
                last_good_idx = i

        return last_good_idx == 0
