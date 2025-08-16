from .a3_dynamic_programming import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    n = 2

    # Act
    result = Solution().climbStairs(n)

    # Assert
    assert result == 2


def test_when_example2_then_return_expected_result():
    # Arrange
    n = 3

    # Act
    result = Solution().climbStairs(n)

    # Assert
    assert result == 3


def test_when_n_equal_1_then_return_1():
    # Arrange
    n = 1

    # Act
    result = Solution().climbStairs(n)

    # Assert
    assert result == 1
