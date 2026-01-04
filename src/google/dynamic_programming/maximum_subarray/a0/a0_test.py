from .a0 import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Act
    result = Solution().maxSubArray(nums)

    # Assert
    assert result == 6
