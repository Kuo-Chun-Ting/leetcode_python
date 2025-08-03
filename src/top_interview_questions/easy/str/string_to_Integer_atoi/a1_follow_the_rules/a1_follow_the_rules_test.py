from .a1_follow_the_rules import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = "42"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == 42


def test_when_example2_then_return_expected_result():
    # Arrange
    s = " -042"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == -42


def test_when_example3_then_return_expected_result():
    # Arrange
    s = "1337c0d3"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == 1337


def test_when_example4_then_return_expected_result():
    # Arrange
    s = "0-1"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == 0


def test_when_example5_then_return_expected_result():
    # Arrange
    s = "words and 987"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == 0


def test_when_number_greater_than_high_boundary_then_return_high_boundary():
    # Arrange
    s = "91283472332"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == 2**31 - 1


def test_when_number_less_than_low_boundary_then_return_low_boundary():
    # Arrange
    s = "-91283472332"

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == -(2**31)


def test_when_empty_string_then_return_0():
    # Arrange
    s = ""

    # Act
    result = Solution().myAtoi(s)

    # Assert
    assert result == 0
