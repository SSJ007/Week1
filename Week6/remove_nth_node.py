# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return

        first = head
        second = head

        for i in  range(n):
            second = second.next

        if second is None:
            return head.next

        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next

        return head

