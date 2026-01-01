class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            width = right - left

            if height[left] > height[right]:
                area = height[right] * width
                right -= 1
            else:
                area = height[left] * width
                left += 1

            max_area = max(max_area, area)

        return max_area
