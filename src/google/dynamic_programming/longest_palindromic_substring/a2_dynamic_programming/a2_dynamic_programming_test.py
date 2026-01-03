from .a2_dynamic_programming import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = "babad"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result in ("bab", "aba")


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


def test_when_example5_then_return_expected_result():
    # Arrange
    s = "ccc"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result == "ccc"


def test_when_example6_then_return_expected_result():
    # Arrange
    s = "abbcccba"

    # Act
    result = Solution().longestPalindrome(s)

    # Assert
    assert result == "bcccb"
