class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            fast_val = nums[fast]
            slow_val = nums[slow]
            if fast_val != slow_val:
                slow += 1
                nums[slow] = fast_val

            fast += 1

        return slow + 1
