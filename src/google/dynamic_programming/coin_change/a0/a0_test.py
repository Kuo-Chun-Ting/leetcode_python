from .a0 import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    coins = [1, 2, 5]
    amount = 11

    # Act
    result = Solution().coinChange(coins, amount)

    # Assert
    assert result == 3


def test_when_example2_then_return_expected_result():
    # Arrange
    coins = [2]
    amount = 3

    # Act
    result = Solution().coinChange(coins, amount)

    # Assert
    assert result == -1
