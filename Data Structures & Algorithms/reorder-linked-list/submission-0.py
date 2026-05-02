# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def revList(self, head):
        prev = None
        curr = head 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev 

    def reorderList(self, head: Optional[ListNode]) -> None:
        # split two halves(first, second)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        second_half = slow.next
        slow.next = None
        first_half = head
        
        rev_second_half = self.revList(second_half)
        first, second = first_half, rev_second_half
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2 

        


        

        