# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 5 -> 3
        # 4 -> 5 -> 6 -> 9
        # 5 -> 0 -> 0 -> 0 -> 1

        # stop the loop when any of them points to null 
        # maintain global carry to track carry 
        # carry = sum of vals//10
        # number to include = sum of vals % 10 
        dummy = node = ListNode()
        first, second = l1, l2
        carry = 0 # 1
        while first and second:
            total = first.val + second.val
            total_with_carry = carry+total #10
            digit = total_with_carry % 10 #0
            carry = total_with_carry // 10
            node.next = ListNode(digit) 
            node = node.next
            first = first.next 
            second = second.next
        remaining = first or second
        while remaining:
            total = remaining.val + carry 
            digit = total % 10
            carry = total // 10
            node.next = ListNode(digit)
            node = node.next
            remaining = remaining.next
        if carry:
            node.next = ListNode(carry)
        return dummy.next
            
