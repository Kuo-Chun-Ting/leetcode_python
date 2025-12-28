from collections import Counter

from .a1_two_pointers import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums = [2, 7, 11, 15]
    target = 9

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert Counter(result) == Counter([1, 2])


def test_when_example2_then_return_expected_result():
    # Arrange
    nums = [2, 3, 4]
    target = 6

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert Counter(result) == Counter([1, 3])


def test_when_example3_then_return_expected_result():
    # Arrange
    nums = [3, 3]
    target = 6

    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert Counter(result) == Counter([1, 2])
