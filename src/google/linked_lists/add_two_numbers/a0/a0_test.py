from ...model import build_list_node

from .a0 import Solution


def test_when_example1_then_return_expected_result():
    # Arrange
    l1 = build_list_node([2, 4, 3])
    l2 = build_list_node([5, 6, 4])

    # Act
    result = Solution().addTwoNumbers(l1, l2)

    # Assert
    assert result == build_list_node([7, 0, 8])


def test_when_example2_then_return_expected_result():
    # Arrange
    l1 = build_list_node([0])
    l2 = build_list_node([0])

    # Act
    result = Solution().addTwoNumbers(l1, l2)

    # Assert
    assert result == build_list_node([0])


def test_when_example3_then_return_expected_result():
    # Arrange
    l1 = build_list_node([9, 9, 9, 9, 9, 9, 9])
    l2 = build_list_node([9, 9, 9, 9])

    # Act
    result = Solution().addTwoNumbers(l1, l2)

    # Assert
    assert result == build_list_node([8, 9, 9, 9, 0, 0, 0, 1])
