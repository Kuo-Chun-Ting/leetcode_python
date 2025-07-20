from .a0 import Solution


def test_when_all_zeros_then_return_itself():
    # Arrange
    nums = [0, 0, 0, 0]

    # Act
    Solution().moveZeroes(nums)

    # Assert
    assert nums == [0, 0, 0, 0]


def test_when_no_zero_then_return_itself():
    # Arrange
    nums = [1, 2, 3, 4]

    # Act
    Solution().moveZeroes(nums)

    # Assert
    assert nums == [1, 2, 3, 4]


def test_when_contain_zero_then_move_zeros_to_end():
    # Arrange
    nums = [0, 1, 0, 3, 12]
    # Act

    Solution().moveZeroes(nums)

    # Assert
    assert nums == [1, 3, 12, 0, 0]


def test_when_contain_zero_then_move_zeros_to_end2():
    # Arrange
    nums = [1, 0, 1]
    # Act

    Solution().moveZeroes(nums)

    # Assert
    assert nums == [1, 1, 0]
