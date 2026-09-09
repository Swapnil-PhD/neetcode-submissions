# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0

        while l1 or l2 or carry:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            total = x1 + x2 + carry
            
            digit = (total) % 10
            carry = (total) // 10

            node.next = ListNode(digit)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next
