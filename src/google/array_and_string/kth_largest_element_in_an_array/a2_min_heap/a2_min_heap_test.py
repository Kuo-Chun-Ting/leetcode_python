from .a2_min_heap import Solution


def normalize_order(three_sum_answers: list[list[int]]) -> list[list[int]]:
    return sorted([sorted(answer) for answer in three_sum_answers])


def test_when_example1_then_return_1():
    # Arrange
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    # Act
    result = Solution().findKthLargest(nums, k)

    # Assert
    assert result == 5


def test_when_example3_then_return_1():
    # Arrange
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    # Act
    result = Solution().findKthLargest(nums, k)

    # Assert
    assert result == 4
