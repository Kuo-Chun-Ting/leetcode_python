from .a1_hash_table import Solution
from collections import Counter


def test_when_no_duplicate_element_then_return_empty_list():
    # Arrange
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]

    # Act
    result = Solution().intersect(nums1, nums2)

    # Assert
    assert Counter([]) == Counter(result)


def test_when_duplicate_elements_exist_once_then_return_intersection_list():
    # Arrange
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 6]

    # Act
    result = Solution().intersect(nums1, nums2)

    # Assert
    assert Counter([2, 3]) == Counter(result)


def test_when_duplicate_elements_existing_twice_then_return_intersection_list():
    # Arrange
    nums1 = [1, 2, 3, 3]
    nums2 = [3, 2, 6, 3]

    # Act
    result = Solution().intersect(nums1, nums2)

    # Assert
    assert Counter([3, 2, 3]) == Counter(result)
