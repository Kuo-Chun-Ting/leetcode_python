from .a1_check_all_substrings import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = "babad"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result == "bab"


def test_when_example2_then_return_expected_result():
    # Arrange
    s = "cbbd"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result == "bb"


def test_when_example3_then_return_expected_result():
    # Arrange
    s = "a"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result == "a"


def test_when_example4_then_return_expected_result():
    # Arrange
    s = "bb"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result == "bb"
