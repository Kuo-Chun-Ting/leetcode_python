from .a2_one_pass import Solution


def test_when_example1_then_return_true():
    # Arrange
    prices = [7, 1, 5, 3, 6, 4]

    # Act
    result = Solution().maxProfit(prices)

    # Assert
    assert result == 5


def test_when_example2_then_return_true():
    # Arrange
    prices = [7, 6, 4, 3, 1]

    # Act
    result = Solution().maxProfit(prices)

    # Assert
    assert result == 0
