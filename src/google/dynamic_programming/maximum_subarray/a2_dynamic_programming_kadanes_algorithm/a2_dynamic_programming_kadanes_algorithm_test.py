from .a2_dynamic_programming_kadanes_algorithm import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Act
    result = Solution().maxSubArray(nums)

    # Assert
    assert result == 6


def test_when_example2_then_return_expected_result():
    # Arrange
    nums = [1]

    # Act
    result = Solution().maxSubArray(nums)

    # Assert
    assert result == 1


def test_when_example3_then_return_expected_result():
    # Arrange
    nums = [5, 4, -1, 7, 8]

    # Act
    result = Solution().maxSubArray(nums)

    # Assert
    assert result == 23
