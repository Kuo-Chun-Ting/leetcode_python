import random


class Solution:

    def __init__(self, nums: list[int]):
        self._nums = nums
        self._backup_nums = nums.copy()

    def reset(self) -> list[int]:
        self._nums[:] = self._backup_nums.copy()
        return self._nums

    def shuffle(self) -> list[int]:
        n = len(self._nums)
        for i in range(n):
            random_idx = random.randint(0, n - 1)
            self._nums[i], self._nums[random_idx] = (
                self._nums[random_idx],
                self._nums[i],
            )
        return self._nums
