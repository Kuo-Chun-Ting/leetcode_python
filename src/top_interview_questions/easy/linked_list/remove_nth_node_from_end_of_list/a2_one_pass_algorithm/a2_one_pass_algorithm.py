from ...model import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy_node = ListNode(val=-1)
        dummy_node.next = head

        first_ptr = dummy_node
        second_ptr = dummy_node

        for _ in range(n):
            second_ptr = second_ptr.next

        while second_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        first_ptr.next = first_ptr.next.next
        return dummy_node.next
