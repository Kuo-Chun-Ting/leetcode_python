from .a0_in_place_modification import Solution


def test_when_k_less_than_length_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    # Act
    Solution().rotate(nums, k)

    # Assert
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_when_k_greater_than_length_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10

    # Act
    Solution().rotate(nums, k)

    # Assert
    assert nums == [5, 6, 7, 1, 2, 3, 4]
