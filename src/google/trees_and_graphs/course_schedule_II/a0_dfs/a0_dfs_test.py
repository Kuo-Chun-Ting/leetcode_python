from .a0_dfs import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    numCourses = 2
    prerequisites = [[1, 0]]

    # Act
    result = Solution().findOrder(numCourses, prerequisites)

    # Assert
    assert len(result) == numCourses


def test_when_example2_then_return_expected_result():
    # Arrange
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    # Act
    result = Solution().findOrder(numCourses, prerequisites)

    # Assert
    assert len(result) == numCourses


def test_when_cycle_exists_then_return_expected_empty_list():
    # Arrange
    numCourses = 2
    prerequisites = [[0,1],[1,0]]

    # Act
    result = Solution().findOrder(numCourses, prerequisites)

    # Assert
    assert result == []


def test_create_graph_when_exapmle1_then_return_expected_result():
    # Arrange
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    # Act
    result = Solution().create_adjacency_list(prerequisites)

    # Assert
    assert result == {
        0: [1, 2],
        1: [3],
        2: [3],
    }
