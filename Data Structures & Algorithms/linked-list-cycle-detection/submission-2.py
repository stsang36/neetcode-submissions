# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        turt = head
        hare = head

        while (turt is not None and hare is not None):
            turt = turt.next
            hare = getattr(hare.next, "next", None)

            if turt is hare and turt is not None:
                return True
        
        return False
        