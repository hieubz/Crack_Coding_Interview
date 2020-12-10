class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy_head = ListNode()
        curr = dummy_head
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry % 10)
            carry = carry // 10
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy_head.next

