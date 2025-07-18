class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_num = 0
        for n in nums:
            single_num ^= n
        return single_num
