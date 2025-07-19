from .a1_schoolbook_addition_with_carry import Solution


def test_when_ones_digist_not_9_then_return_expected_result():
    # Arrange
    nums = [1, 2, 3]

    # Act
    result = Solution().plusOne(nums)

    # Assert
    assert result == [1, 2, 4]


def test_when_ones_digist_is_9_then_return_expected_result():
    # Arrange
    nums = [1, 2, 9]

    # Act
    result = Solution().plusOne(nums)

    # Assert
    assert result == [1, 3, 0]


def test_when_all_digist_is_9_then_return_expected_result():
    # Arrange
    nums = [9, 9, 9]

    # Act
    result = Solution().plusOne(nums)

    # Assert
    assert result == [1, 0, 0, 0]
