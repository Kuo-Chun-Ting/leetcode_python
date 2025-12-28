class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements: dict[int, int] = {}
        for idx, n in enumerate(nums):
            complement = target - n

            if n in complements:
                return [idx, complements[n]]
            complements[complement] = idx

        return []
