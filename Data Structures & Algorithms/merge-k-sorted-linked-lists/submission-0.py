# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # brute force 
        temp_arr_node = []

        for lst in lists:
            while lst:
                temp_arr_node.append(lst.val)
                lst = lst.next
        temp_arr_node.sort()


        #dummy node
        dummy = ListNode()
        curr = dummy

        for node in temp_arr_node:
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next
