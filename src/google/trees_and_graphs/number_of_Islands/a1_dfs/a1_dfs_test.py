from .a1_dfs import Solution


def test_when_example1_then_return_1():
    # Arrange
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    # Act
    result = Solution().numIslands(grid)

    # Assert
    assert result == 1


def test_when_example2_then_return_3():
    # Arrange
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    # Act
    result = Solution().numIslands(grid)

    # Assert
    assert result == 3


def test_when_example3_then_return_3():
    # Arrange
    grid = [
        ["1"],
        ["1"],
    ]

    # Act
    result = Solution().numIslands(grid)

    # Assert
    assert result == 1


def test_when_example4_then_return_3():
    # Arrange
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]

    # Act
    result = Solution().numIslands(grid)

    # Assert
    assert result == 0
