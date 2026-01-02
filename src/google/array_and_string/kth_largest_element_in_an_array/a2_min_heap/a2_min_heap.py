import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        value = 0
        for _ in range(len(nums) - k + 1):
            value = heapq.heappop(nums)

        return value
