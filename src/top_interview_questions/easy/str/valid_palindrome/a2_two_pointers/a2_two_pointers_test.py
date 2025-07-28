from .a2_two_pointers import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = "A man, a plan, a canal: Panama"
    # Act
    result = Solution().isPalindrome(s)

    # Assert
    assert result is True


def test_when_example2_then_return_expected_result():
    # Arrange
    s = "race a car"
    # Act
    result = Solution().isPalindrome(s)

    # Assert
    assert result is False


def test_when_example3_then_return_expected_result():
    # Arrange
    s = " "
    # Act
    result = Solution().isPalindrome(s)

    # Assert
    assert result is True


def test_when_example4_then_return_expected_result():
    # Arrange
    s = " "
    # Act
    result = Solution().isPalindrome(s)

    # Assert
    assert result is True
