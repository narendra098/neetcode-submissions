# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        headToLeft = ListNode()
        rightToTail = None
        midHead = midNode = ListNode()
        if left == right:
            return head
        
        curr = head 
        c = 0
        while curr:
            c += 1
            if c == left-1:
                temp = curr.next 
                curr.next = None
                headToLeft = head 
                curr = temp
            elif c in (num for num in range(left, right)):
                midNode.next = curr
                midNode = midNode.next
                curr = curr.next
            elif c == right:
                temp = curr.next
                midNode.next = curr
                midNode.next.next = None
                rightToTail = temp
                break
            else:
                curr = curr.next
        
        revMid = self.rev(midHead.next)

        currLeft = headToLeft
        while currLeft.next:
            currLeft = currLeft.next
        

        currMid = revMid
        while currMid.next:
            currMid = currMid.next

        currLeft.next = revMid
        currMid.next = rightToTail

        if left == 1:
            return headToLeft.next
        else:
            return headToLeft