class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        num_dict: dict[int, int] = {}
        for n in nums:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                num_dict[n] += 1

        for k, v in num_dict.items():
            if v == 1:
                return k

        return -1
