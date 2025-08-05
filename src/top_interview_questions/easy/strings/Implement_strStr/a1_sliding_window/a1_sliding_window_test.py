from .a1_sliding_window import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    haystack = "sadbutsad"
    needle = "sad"

    # Act
    result = Solution().strStr(haystack, needle)

    # Assert
    assert result == 0


def test_when_example2_then_return_expected_result():
    # Arrange
    haystack = "leetcode"
    needle = "leeto"

    # Act
    result = Solution().strStr(haystack, needle)

    # Assert
    assert result == -1


def test_when_needle_len_greater_than_haystack_then_return_expected_result():
    # Arrange
    haystack = "a"
    needle = "ll"

    # Act
    result = Solution().strStr(haystack, needle)

    # Assert
    assert result == -1


def test_when_substring_show_in_second_scan_then_return_expected_result():
    # Arrange
    haystack = "mississippi"
    needle = "issip"

    # Act
    result = Solution().strStr(haystack, needle)

    # Assert
    assert result == 4


def test_when_the_same_len_then_return_expected_result():
    # Arrange
    haystack = "a"
    needle = "a"

    # Act
    result = Solution().strStr(haystack, needle)

    # Assert
    assert result == 0
