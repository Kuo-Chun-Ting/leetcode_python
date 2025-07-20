class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        non_zero_idx = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[non_zero_idx] = nums[non_zero_idx], nums[i]
                non_zero_idx += 1
