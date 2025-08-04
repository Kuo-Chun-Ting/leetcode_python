from .a2_frequency_counter import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = "anagram"
    t = "nagaram"

    # Act
    result = Solution().isAnagram(s, t)

    # Assert
    assert result is True


def test_when_example2_then_return_expected_result():
    # Arrange
    s = "rat"
    t = "car"

    # Act
    result = Solution().isAnagram(s, t)

    # Assert
    assert result is False
