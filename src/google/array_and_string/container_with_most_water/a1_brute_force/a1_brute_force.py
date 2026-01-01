class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_capacity = 0

        for i in range(len(height)):
            from_height = height[i]

            for j in range(i + 1, len(height)):
                to_height = height[j]
                curr_capacity = min(from_height, to_height) * (j - i)
                max_capacity = max(max_capacity, curr_capacity)

        return max_capacity
