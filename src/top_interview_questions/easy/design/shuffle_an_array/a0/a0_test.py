from .a0 import Solution


def test_when_example1_then_result_should_be_expected():
    # Arrange
    arr = [1, 2, 3]
    solution = Solution(arr)

    # Act & Assert
    solution.shuffle()
    assert sorted(arr) == [1, 2, 3]

    solution.reset()
    assert arr == [1, 2, 3]

    solution.shuffle()
    assert sorted(arr) == [1, 2, 3]
