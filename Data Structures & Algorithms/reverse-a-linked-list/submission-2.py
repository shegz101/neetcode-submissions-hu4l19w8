# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The two pointer approach


        curr, prev = head, None

        while curr:
            nxt_head = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_head
        
        return prev