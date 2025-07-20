class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict: dict[int, int] = {}
        for i, n in enumerate(nums):
            key = target - n
            val = i

            if n in num_dict:
                return [i, num_dict[n]]
            num_dict[key] = val

        return []
