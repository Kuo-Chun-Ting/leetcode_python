from .a0_two_pointers import Solution


def test_when_no_one_num_then_return_itself():
    # Arrange
    nums = [1]

    # Act
    result = Solution().removeDuplicates(nums)

    # Assert
    expected_nums = nums[:result]

    assert result == 1
    assert expected_nums == [1]


def test_when_no_duplicate_then_return_itself():
    # Arrange
    nums = [1, 2, 3, 4, 5]

    # Act
    result = Solution().removeDuplicates(nums)

    # Assert
    expected_nums = nums[:result]

    assert result == 5
    assert expected_nums == [1, 2, 3, 4, 5]


def test_when_one_duplicate_then_return_itself():
    # Arrange
    nums = [1, 2, 2, 3, 4, 5]

    # Act
    result = Solution().removeDuplicates(nums)

    # Assert
    expected_nums = nums[:result]

    assert result == 5
    assert expected_nums == [1, 2, 3, 4, 5]


def test_when_two_duplicates_then_return_itself():
    # Arrange
    nums = [1, 2, 2, 3, 4, 4, 5]

    # Act
    result = Solution().removeDuplicates(nums)

    # Assert
    expected_nums = nums[:result]

    assert result == 5
    assert expected_nums == [1, 2, 3, 4, 5]


def test_when_long_duplicate_then_return_expected_result():
    # Arrange
    nums = [1, 2, 2, 2, 2, 3, 4, 5]

    # Act
    result = Solution().removeDuplicates(nums)

    # Assert
    expected_nums = nums[:result]

    assert result == 5
    assert expected_nums == [1, 2, 3, 4, 5]
