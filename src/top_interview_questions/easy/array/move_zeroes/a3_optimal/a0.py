class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            zero_idx = i

            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1

            if j == len(nums):
                break

            non_zero_idx = j
            nums[zero_idx], nums[non_zero_idx] = nums[non_zero_idx], nums[zero_idx]
