# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        turt = head
        hare = head

        while (hare is not None and hare.next is not None):
            turt = turt.next
            hare = hare.next.next

            if turt is hare:
                return True
        
        return False
        