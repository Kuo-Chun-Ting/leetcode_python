from .a0_greedy import Solution


def test_when_example1_then_return_1():
    # Arrange
    nums = [2, 3, 1, 1, 4]

    # Act
    result = Solution().canJump(nums)

    # Assert
    assert result is True


def test_when_example2_then_return_1():
    # Arrange
    nums = [3, 2, 1, 0, 4]

    # Act
    result = Solution().canJump(nums)

    # Assert
    assert result is False
