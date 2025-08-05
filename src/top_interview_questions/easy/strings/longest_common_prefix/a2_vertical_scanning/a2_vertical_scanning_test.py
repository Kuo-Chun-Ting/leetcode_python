from .a2_vertical_scanning import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = ["flower", "flow", "flight"]

    # Act
    result = Solution().longestCommonPrefix(s)

    # Assert
    assert result == "fl"


def test_when_example2_then_return_expected_result():
    # Arrange
    s = ["dog", "racecar", "car"]

    # Act
    result = Solution().longestCommonPrefix(s)

    # Assert
    assert result == ""


def test_when_empty_string_then_return_expected_result():
    # Arrange
    s = ["", "racecar", "car"]

    # Act
    result = Solution().longestCommonPrefix(s)

    # Assert
    assert result == ""
