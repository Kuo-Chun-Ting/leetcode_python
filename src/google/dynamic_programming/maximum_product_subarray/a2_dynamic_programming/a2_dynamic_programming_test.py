from .a2_dynamic_programming import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums = [2, 3, -2, 4]

    # Act
    result = Solution().maxProduct(nums)

    # Assert
    assert result == 6


def test_when_example2_then_return_expected_result():
    # Arrange
    nums = [-2, 0, -1]

    # Act
    result = Solution().maxProduct(nums)

    # Assert
    assert result == 0


def test_when_example3_then_return_expected_result():
    # Arrange
    nums = [-4, -3, -2]

    # Act
    result = Solution().maxProduct(nums)

    # Assert
    assert result == 12
