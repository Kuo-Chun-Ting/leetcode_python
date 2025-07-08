from ...model import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy_node = ListNode(val=-1)
        dummy_node.next = head
        curr_node = dummy_node
        length = 0

        while curr_node.next:
            length += 1
            curr_node = curr_node.next

        idx_to_remove = length - n + 1
        curr_node = dummy_node
        curr_idx = 0
        while curr_idx < idx_to_remove - 1:
            curr_idx += 1
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next
        return dummy_node.next
