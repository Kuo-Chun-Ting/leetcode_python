from .a1_monotonic_stack import Solution


def test_when_example1_then_return_1():
    # Arrange
    arr = [10, 13, 12, 14, 15]

    # Act
    result = Solution().oddEvenJumps(arr)

    # Assert
    assert result == 2


def test_when_example2_then_return_1():
    # Arrange
    arr = [2, 3, 1, 1, 4]

    # Act
    result = Solution().oddEvenJumps(arr)

    # Assert
    assert result == 3


def test_when_example3_then_return_1():
    # Arrange
    arr = [1, 2, 3]

    # Act
    result = Solution().oddEvenJumps(arr)

    # Assert
    assert result == 2


def test_when_example4_then_return_1():
    # Arrange
    arr = [5, 4, 4, 2]

    # Act
    result = Solution().oddEvenJumps(arr)

    # Assert
    assert result == 2


def test_when_example5_then_return_1():
    # Arrange
    arr = [5, 1, 3, 4, 2]

    # Act
    result = Solution().oddEvenJumps(arr)

    # Assert
    assert result == 3
