from ...model import ListNode


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow, fast = slow.next, fast.next.next

        return True
