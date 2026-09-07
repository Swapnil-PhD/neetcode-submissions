# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, prev = head, None

        # Reverse the list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Remove nth node and reverse back
        count = 0
        curr1, prev1 = prev, None

        while curr1:
            count += 1

            if count == n:
                curr1 = curr1.next
                continue

            nxt1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = nxt1
            
        return prev1