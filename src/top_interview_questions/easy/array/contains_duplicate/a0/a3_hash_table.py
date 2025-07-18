class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)

        return False
