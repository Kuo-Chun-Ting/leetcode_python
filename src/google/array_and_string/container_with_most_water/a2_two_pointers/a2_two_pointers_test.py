from .a2_two_pointers import Solution


def test_when_example1_then_return_1():
    # Arrange
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # Act
    result = Solution().maxArea(height)

    # Assert
    assert result == 49


def test_when_example2_then_return_1():
    # Arrange
    height = [1, 1]

    # Act
    result = Solution().maxArea(height)

    # Assert
    assert result == 1
