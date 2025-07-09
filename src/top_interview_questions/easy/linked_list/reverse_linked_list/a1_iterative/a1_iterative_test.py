from ...model import ListNode
from .a1_iterative import Solution


def test_when_one_node_then_return_expected_result():
    # Arrange
    head = ListNode(val=1)

    # Act
    result = Solution().reverseList(head)

    # Assert
    assert result.val == 1


def test_when_two_nodes_then_return_expected_result():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    n = 2

    # Act
    result = Solution().reverseList(head)

    # Assert
    assert result.val == 2
    assert result.next.val == 1


def test_when_three_nodes_then_return_expected_result():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=3)

    # Act
    result = Solution().reverseList(head)

    # Assert
    assert result.val == 3
    assert result.next.val == 2
    assert result.next.next.val == 1
