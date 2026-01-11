class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        curr_max = nums[0]
        curr_min = nums[0]
        max_product = nums[0]

        for i in range(1, n):
            curr_num = nums[i]
            curr_max, curr_min = max(
                curr_num, curr_max * curr_num, curr_min * curr_num
            ), min(curr_num, curr_max * curr_num, curr_min * curr_num)

            max_product = max(max_product, curr_max)

        return max_product
