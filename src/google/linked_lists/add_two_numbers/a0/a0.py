from ...model import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            sum = val_1 + val_2 + carry
            carry = 0

            if sum >= 10:
                sum = sum % 10
                carry = 1

            curr.next = ListNode(val=sum)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry == 1:
            curr.next = ListNode(val=1)

        return dummy.next
