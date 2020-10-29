# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode):
    #     dummyHead = curr = ListNode(0)
    #     carry = 0
    #     while l1 or l2:
    #         # return 0 if linklist is null
    #         x = l1.val if l1 else 0
    #         y = l2.val if l2 else 0
    #
    #         # sum up
    #         sums = carry + x + y
    #
    #         # get the memorial number
    #         carry = sums // 10
    #
    #         # add to new link_list
    #         curr.next = ListNode(sums % 10)
    #
    #         # set current node next
    #         curr = curr.next
    #
    #         # continue
    #         if l1:
    #             l1 = l1.next
    #         if l2:
    #             l2 = l2.next
    #
    #     # if carry > 0 => add the last element to list
    #     if carry > 0:
    #         curr.next = ListNode(carry)
    #
    #     return dummyHead.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummyHead = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry = carry // 10

        return dummyHead.next
