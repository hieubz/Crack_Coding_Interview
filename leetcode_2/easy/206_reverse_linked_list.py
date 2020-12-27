# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode):
        reverse_list = None

        while head is not None:
            curr = head
            head = head.next
            curr.next = reverse_list
            reverse_list = curr

        return reverse_list