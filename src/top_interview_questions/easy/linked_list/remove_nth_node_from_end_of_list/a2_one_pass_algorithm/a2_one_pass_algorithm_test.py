from ...model import ListNode
from .a2_one_pass_algorithm import Solution


def test_when_one_node_return_none():
    # Arrange
    head = ListNode(val=1)
    n = 1

    # Act
    result = Solution().removeNthFromEnd(head, n)

    # Assert
    assert result is None


def test_when_two_nodes_and_remove_fisrt_then_return_last_node():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    n = 2

    # Act
    result = Solution().removeNthFromEnd(head, n)

    # Assert
    assert result.val == 2
    assert result.next == None


def test_when_two_nodes_and_remove_last_then_return_fist_node():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    n = 1

    # Act
    result = Solution().removeNthFromEnd(head, n)

    # Assert
    assert result.val == 1
    assert result.next == None
