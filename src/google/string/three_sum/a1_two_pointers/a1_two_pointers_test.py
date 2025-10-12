from .a1_two_pointers import Solution


def test_when_example1_then_return_1():
    # Arrange
    nums = [-1, 0, 1, 2, -1, -4]

    # Act
    result = Solution().threeSum(nums)

    # Assert
    assert result == [[-1, -1, 2], [-1, 0, 1]]


def test_when_example2_then_return_1():
    # Arrange
    nums = [0, 1, 1]

    # Act
    result = Solution().threeSum(nums)

    # Assert
    assert result == []


def test_when_example3_then_return_1():
    # Arrange
    nums = [0, 0, 0]

    # Act
    result = Solution().threeSum(nums)

    # Assert
    assert result == [[0, 0, 0]]
