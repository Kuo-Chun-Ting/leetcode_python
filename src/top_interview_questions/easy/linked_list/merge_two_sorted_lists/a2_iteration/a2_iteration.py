from ...model import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy_node = ListNode(val=-1)
        curr_node = dummy_node

        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next

            curr_node = curr_node.next

        curr_node.next = list1 if list1 else list2
        return dummy_node.next
