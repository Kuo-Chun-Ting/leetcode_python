from .a1_rotate_groups_of_four_cells import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    matirx = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    # Act
    Solution().rotate(matirx)

    # Assert
    assert matirx == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
