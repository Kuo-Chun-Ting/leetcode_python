from .a4_using_reverse import Solution


def test_reverse_when_one_num_then_return_it():
    # Arrange
    nums = [1]

    # Act
    Solution().reverse(nums, 0, len(nums) - 1)

    # Assert
    assert nums == [1]


def test_reverse_when_odd_nums_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3]

    # Act
    Solution().reverse(nums, 0, len(nums) - 1)

    # Assert
    assert nums == [3, 2, 1]


def test_reverse_when_even_nums_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3, 4]

    # Act
    Solution().reverse(nums, 0, len(nums) - 1)

    # Assert
    assert nums == [4, 3, 2, 1]


def test_rotate_when_k_less_than_length_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    # Act
    Solution().rotate(nums, k)

    # Assert
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_when_k_greater_than_length_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10

    # Act
    Solution().rotate(nums, k)

    # Assert
    assert nums == [5, 6, 7, 1, 2, 3, 4]
