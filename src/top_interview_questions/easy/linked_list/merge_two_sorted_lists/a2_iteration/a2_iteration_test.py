from ...model import ListNode
from .a2_iteration import Solution


def test_when_no_node_return_none():
    # Arrange
    list1 = None
    list2 = None

    # Act
    result = Solution().mergeTwoLists(list1, list2)

    # Assert
    assert result is None


def test_when_list1_none_then_return_list2():
    # Arrange
    list1 = None
    list2 = ListNode(val=1)
    list2.next = ListNode(val=2)

    # Act
    result = Solution().mergeTwoLists(list1, list2)

    # Assert
    assert result == list2


def test_when_list2_none_then_return_list1():
    # Arrange
    list2 = None
    list1 = ListNode(val=1)
    list1.next = ListNode(val=2)

    # Act
    result = Solution().mergeTwoLists(list1, list2)

    # Assert
    assert result == list1


def test_when_all_list2_greater_than_list1_then_return_expected_result():
    # Arrange
    list1 = ListNode(val=1)
    list1.next = ListNode(val=2)
    list2 = ListNode(val=3)
    list2.next = ListNode(val=4)

    # Act
    result = Solution().mergeTwoLists(list1, list2)

    # Assert
    assert result and result.val == 1
    assert result.next and result.next.val == 2
    assert result.next.next and result.next.next.val == 3
    assert result.next.next.next and result.next.next.next.val == 4


def test_when_all_list1_greater_than_list2_then_return_expected_result():
    # Arrange
    list1 = ListNode(val=3)
    list1.next = ListNode(val=4)
    list2 = ListNode(val=1)
    list2.next = ListNode(val=2)

    # Act
    result = Solution().mergeTwoLists(list1, list2)

    # Assert
    assert result and result.val == 1
    assert result.next and result.next.val == 2
    assert result.next.next and result.next.next.val == 3
    assert result.next.next.next and result.next.next.next.val == 4


def test_when_list1_and_list2_have_alternating_values_then_return_merged_sorted_list():
    # Arrange
    list1 = ListNode(val=1)
    list1.next = ListNode(val=4)
    list2 = ListNode(val=2)
    list2.next = ListNode(val=3)

    # Act
    result = Solution().mergeTwoLists(list1, list2)

    # Assert
    assert result and result.val == 1
    assert result.next and result.next.val == 2
    assert result.next.next and result.next.next.val == 3
    assert result.next.next.next and result.next.next.next.val == 4
