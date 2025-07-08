from ...model import ListNode
from .a1_data_overwriting import Solution


def test_when_delete_first_node_return_expected_result():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=3)

    # Act
    Solution().deleteNode(head)

    # Assert
    assert head.val == 2
    assert head.next.val == 3


def test_when_delete_middle_node_then_return_expected_result():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=3)

    # Act
    Solution().deleteNode(head.next)

    # Assert
    assert head.val == 1
    assert head.next.val == 3
