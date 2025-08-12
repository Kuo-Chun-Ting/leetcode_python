from .a3_three_pointers_start_from_the_end import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # Act
    Solution().merge(nums1, m, nums2, n)

    # Assert
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_when_example2_then_return_expected_result():
    # Arrange
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    # Act
    Solution().merge(nums1, m, nums2, n)

    # Assert
    assert nums1 == [1]


def test_when_example3_then_return_expected_result():
    # Arrange
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    # Act
    Solution().merge(nums1, m, nums2, n)

    # Assert
    assert nums1 == [1]


def test_when_example4_then_return_expected_result():
    # Arrange
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1

    # Act
    Solution().merge(nums1, m, nums2, n)

    # Assert
    assert nums1 == [1, 2]
