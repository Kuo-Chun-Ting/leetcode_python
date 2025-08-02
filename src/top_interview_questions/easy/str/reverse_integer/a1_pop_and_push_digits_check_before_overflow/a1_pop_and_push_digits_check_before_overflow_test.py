from .a1_pop_and_push_digits_check_before_overflow import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    x = 123
    # Act
    result = Solution().reverse(x)

    # Assert
    assert result == 321


def test_when_example2_then_return_expected_result():
    # Arrange
    x = -123
    # Act
    result = Solution().reverse(x)

    # Assert
    assert result == -321


def test_when_example3_then_return_expected_result():
    # Arrange
    x = 120

    # Act
    result = Solution().reverse(x)

    # Assert
    assert result == 21
