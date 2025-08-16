from .a2_dynamic_programming import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums = [1,2,3,1]

    # Act
    result = Solution().rob(nums)

    # Assert
    assert result == 4


def test_when_example2_then_return_expected_result():
    # Arrange
    nums = [2,7,9,3,1]

    # Act
    result = Solution().rob(nums)

    # Assert
    assert result == 12
