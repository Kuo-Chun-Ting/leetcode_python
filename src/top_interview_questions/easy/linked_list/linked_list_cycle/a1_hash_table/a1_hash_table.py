from ...model import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        ptr_set = set()

        while head:
            if id(head) in ptr_set:
                return True
            ptr_set.add(id(head))
            head = head.next

        return False
