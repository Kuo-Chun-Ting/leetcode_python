class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = curr = nums[0]

        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            max_sum = max(max_sum, curr)

        return max_sum
