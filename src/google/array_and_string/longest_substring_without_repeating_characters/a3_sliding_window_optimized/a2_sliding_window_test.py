from .a2_sliding_window import Solution


def test_when_example1_then_return_1():
    # Arrange
    string = "abcabcbb"

    # Act
    result = Solution().lengthOfLongestSubstring(string)

    # Assert
    assert result == 3


def test_when_example2_then_return_1():
    # Arrange
    string = "bbbbb"

    # Act
    result = Solution().lengthOfLongestSubstring(string)

    # Assert
    assert result == 1


def test_when_example3_then_return_1():
    # Arrange
    string = "pwwkew"

    # Act
    result = Solution().lengthOfLongestSubstring(string)

    # Assert
    assert result == 3


def test_when_example4_then_return_1():
    # Arrange
    string = "abcbrt"

    # Act
    result = Solution().lengthOfLongestSubstring(string)

    # Assert
    assert result == 4
    
def test_when_example5_then_return_1():
    # Arrange
    string = "abba"

    # Act
    result = Solution().lengthOfLongestSubstring(string)

    # Assert
    assert result == 2
