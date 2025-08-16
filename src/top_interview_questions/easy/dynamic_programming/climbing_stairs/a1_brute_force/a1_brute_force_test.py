from .a1_brute_force import Solution


def test_when_example1_then_return_true():
    # Arrange
    n = 2

    # Act
    result = Solution().climbStairs(n)

    # Assert
    assert result == 2


def test_when_example2_then_return_true():
    # Arrange
    n = 3

    # Act
    result = Solution().climbStairs(n)

    # Assert
    assert result == 3
