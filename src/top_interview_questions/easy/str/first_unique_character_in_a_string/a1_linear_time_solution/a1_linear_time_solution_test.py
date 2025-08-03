from .a1_linear_time_solution import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    s = "leetcode"

    # Act
    result = Solution().firstUniqChar(s)

    # Assert
    assert result == 0


def test_when_example2_then_return_expected_result():
    # Arrange
    s = "loveleetcode"
    # Act
    result = Solution().firstUniqChar(s)

    # Assert
    assert result == 2


def test_when_example3_then_return_expected_result():
    # Arrange
    s = "aabb"

    # Act
    result = Solution().firstUniqChar(s)

    # Assert
    assert result == -1
