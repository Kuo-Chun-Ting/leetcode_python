class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sum_pairs: list[list[int]] = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                break

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            two_sum_pairs = self.twoSum(sorted_nums, i + 1, -sorted_nums[i])

            for two_sum_pair in two_sum_pairs:
                three_sum_pair = [sorted_nums[i], two_sum_pair[0], two_sum_pair[1]]
                three_sum_pairs.append(three_sum_pair)

        return three_sum_pairs

    def twoSum(self, nums: list[int], from_idx: int, target: int) -> list[list[int]]:
        two_sum_pairs: list[list[int]] = []
        complements: set[int] = set()

        i = from_idx
        while i < len(nums):
            complement = target - nums[i]

            if complement in complements:
                two_sum_pairs.append([complement, nums[i]])
                i += 1

                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
            else:
                complements.add(nums[i])
                i += 1

        return two_sum_pairs
