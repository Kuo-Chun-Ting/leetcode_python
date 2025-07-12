from ...model import ListNode
from .a0_reverse_first_half_In_place import Solution


def test_when_one_node_return_true():
    # Arrange
    head = ListNode(val=1)

    # Act
    result = Solution().isPalindrome(head)

    # Assert
    assert result is True


def test_when_two_valid_nodes_return_true():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=1)

    # Act
    result = Solution().isPalindrome(head)

    # Assert
    assert result is True


def test_when_two_invalid_nodes_return_false():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)

    # Act
    result = Solution().isPalindrome(head)

    # Assert
    assert result is False


def test_when_three_valid_nodes_return_true():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=1)

    # Act
    result = Solution().isPalindrome(head)

    # Assert
    assert result is True


def test_when_two_invalid_nodes_return_true():
    # Arrange
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=2)

    # Act
    result = Solution().isPalindrome(head)

    # Assert
    assert result is False
