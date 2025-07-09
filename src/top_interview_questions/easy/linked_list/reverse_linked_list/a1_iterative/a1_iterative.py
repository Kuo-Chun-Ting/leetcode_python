from ...model import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr_node = head
        prev_node = None

        while curr_node:
            next_temp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_temp_node

        return prev_node
