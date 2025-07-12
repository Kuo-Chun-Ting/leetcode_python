from ...model import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:

        dummy_node = ListNode(val=-1)
        dummy_node.next = head
        curr_node = dummy_node
        length = 0

        while curr_node.next:
            length += 1
            curr_node = curr_node.next

        if length == 1:
            return True

        mid = length // 2
        curr_node = head
        rev = None
        for _ in range(mid):
            curr_node.next, rev, curr_node = (rev, curr_node, curr_node.next)

        second_half = curr_node if length % 2 == 0 else curr_node.next

        if rev is None and second_half is None:
            return True

        while rev and second_half:
            if rev.val != second_half.val:
                return False

            rev = rev.next
            second_half = second_half.next

        return True
