from .a2_peak_valley_approach import Solution


def test_when_one_price_then_return_0():
    # Arrange
    nums = [7]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 0


def test_when_no_profit_then_return_0():
    # Arrange
    nums = [7, 6, 4, 3, 1]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 0


def test_when_one_peak_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3, 4, 5]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 4


def test_when_two_peaks_then_return_expected_result():
    # Arrange
    nums = [7, 1, 5, 3, 6, 4]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 7


def test_when_two_peaks_then_return_expected_results():
    # Arrange
    nums = [2, 1, 2, 0, 1]

    # Act
    result = Solution().maxProfit(nums)

    # Assert
    assert result == 2