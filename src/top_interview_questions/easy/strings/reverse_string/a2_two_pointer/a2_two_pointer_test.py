from .a2_two_pointer import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = ["h", "e", "l", "l", "o"]

    # Act
    Solution().reverseString(s)

    # Assert
    assert s == ["o", "l", "l", "e", "h"]


def test_when_example2_then_return_expected_result():
    # Arrange
    s = ["H", "a", "n", "n", "a", "h"]

    # Act
    Solution().reverseString(s)

    # Assert
    assert s == ["h", "a", "n", "n", "a", "H"]
