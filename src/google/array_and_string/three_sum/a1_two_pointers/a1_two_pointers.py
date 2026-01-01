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
        left, right = from_idx, len(nums) - 1
        two_sum_pairs: list[list[int]] = []

        while left < right:
            two_sum = nums[left] + nums[right]

            if two_sum > target:
                right -= 1
                continue

            if two_sum < target:
                left += 1
                continue

            two_sum_pairs.append([nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        return two_sum_pairs
