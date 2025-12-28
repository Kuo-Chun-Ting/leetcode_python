from .a2_one_pass import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums = [7, 1, 5, 3, 6, 4]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 5


def test_when_one_peak_then_return_expected_result():
    # Arrange
    nums = [7, 6, 4, 3, 1]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 0
