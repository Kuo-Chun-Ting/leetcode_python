class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        k_max = 0

        for i in range(n - 1, n - 1 - k, -1):
            k_max = sorted_nums[i]

        return k_max
