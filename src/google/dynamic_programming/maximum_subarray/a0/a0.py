class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = float("-inf")

        for i in range(n):
            for j in range(i, n):
                curr_sum = 0
                for k in range(i, j + 1):
                    curr_sum += nums[k]

                max_sum = max(max_sum, curr_sum)

        return max_sum
