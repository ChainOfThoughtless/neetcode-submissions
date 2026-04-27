# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev = head
            curr = head.next
            prev.next = None
            while curr:
                next = curr.next
                curr.next = prev
                head = curr
                prev = curr
                curr = next
        return head
        # 2->3->1->4
        # p  c  n