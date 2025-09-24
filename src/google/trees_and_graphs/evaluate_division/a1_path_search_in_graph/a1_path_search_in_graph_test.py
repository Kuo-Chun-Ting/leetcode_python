from .a1_path_search_in_graph import Solution


def test_when_example1_then_return_1():
    # Arrange
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    # Act
    result = Solution().calcEquation(equations, values, queries)

    # Assert
    assert result == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]


def test_create_graph_when_exapmle1_then_return_expected_result():
    # Arrange
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]

    # Act
    result = Solution().create_graph(equations, values)

    # Assert
    assert result == {
        "a": [("b", 2.0)],
        "b": [("a", 0.5), ("c", 3.0)],
        "c": [("b", 1 / 3)],
    }


def test_dfs_when_a_c_then_return_expected_result():
    # Arrange
    graph: dict[str, list[tuple[str, float]]] = {
        "a": [("b", 2.0)],
        "b": [("a", 0.5), ("c", 3.0)],
        "c": [("b", 1 / 3)],
    }

    # Act
    result = Solution().dfs(start="a", target="c", graph=graph)

    # Assert
    assert result == 6


def test_dfs_when_b_a_then_return_expected_result():
    # Arrange
    graph: dict[str, list[tuple[str, float]]] = {
        "a": [("b", 2.0)],
        "b": [("a", 0.5), ("c", 3.0)],
        "c": [("b", 1 / 3)],
    }

    # Act
    result = Solution().dfs(start="b", target="a", graph=graph)

    # Assert
    assert result == 0.5
