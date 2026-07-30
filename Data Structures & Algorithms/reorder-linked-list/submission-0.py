# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None

        while current:

            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev



    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = self.reverse(slow.next)
        slow.next = None

        while second:

            n1, n2 = first.next, second.next

            first.next = second
            second.next = n1
            first = n1
            second = n2



    
    

