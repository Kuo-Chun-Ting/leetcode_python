from ...model import ListNode
from .a1_hash_table import Solution


def test_when_one_node_and_no_cycle_then_return_false():
    # Arrange
    head = ListNode(val=1)

    # Act
    result = Solution().hasCycle(head)

    # Assert
    assert result is False


def test_when_one_node_and_has_cycle_then_return_true():
    # Arrange
    head = ListNode(val=1)
    head.next = head

    # Act
    result = Solution().hasCycle(head)

    # Assert
    assert result is True


def test_when_three_node_and_no_cycle_then_return_false():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=2)

    # Act
    result = Solution().hasCycle(head)

    # Assert
    assert result is False


def test_when_three_node_and_has_cycle_then_return_true():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = head

    # Act
    result = Solution().hasCycle(head)

    # Assert
    assert result is True
