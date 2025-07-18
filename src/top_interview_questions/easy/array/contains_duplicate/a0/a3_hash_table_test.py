from .a3_hash_table import Solution


def test_when_one_num_then_return_false():
    # Arrange
    nums = [1]

    # Act
    result = Solution().containsDuplicate(nums)

    # Assert
    assert result is False


def test_when_no_duplicate_then_return_true():
    # Arrange
    nums = [1, 2, 3]

    # Act
    result = Solution().containsDuplicate(nums)

    # Assert
    assert result is False


def test_when_contain_duplicate_then_return_true():
    # Arrange
    nums = [1, 2, 2, 4]

    # Act
    result = Solution().containsDuplicate(nums)

    # Assert
    assert result is True
