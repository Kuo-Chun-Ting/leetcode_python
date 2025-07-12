from ...model import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, rev, slow = rev, slow, slow.next

        if fast:
            slow = slow.next

        while slow:
            if slow.val != rev.val:
                return False

            slow = slow.next
            rev = rev.next

        return True
