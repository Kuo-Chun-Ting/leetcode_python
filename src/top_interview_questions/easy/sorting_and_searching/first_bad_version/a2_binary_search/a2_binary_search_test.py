from unittest.mock import patch

from . import a2_binary_search
from .a2_binary_search import Solution


def test_when_example1_then_return_expected_result_first_bad_version():
    # Arrange
    n, bad, expected = 5, 4, 4

    # Act
    with patch.object(a2_binary_search, "isBadVersion", side_effect=lambda v: v >= bad):
        result = Solution().firstBadVersion(n)

    # Assert
    assert result == expected


def test_when_example2_then_return_expected_result_first_bad_version():
    # Arrange
    n, bad, expected = 1, 1, 1

    # Act
    with patch.object(a2_binary_search, "isBadVersion", side_effect=lambda v: v >= bad):
        result = Solution().firstBadVersion(n)

    # Assert
    assert result == expected


def test_when_example3_then_return_expected_result_first_bad_version():
    n, bad, expected = 10, 7, 7
    with patch.object(a2_binary_search, "isBadVersion", side_effect=lambda v: v >= bad):
        result = Solution().firstBadVersion(n)
    assert result == expected


def test_when_example4_then_return_expected_result_first_bad_version():
    # Arrange
    n, bad, expected = 10, 10, 10

    # Act
    with patch.object(a2_binary_search, "isBadVersion", side_effect=lambda v: v >= bad):
        result = Solution().firstBadVersion(n)

    # Assert
    assert result == expected
