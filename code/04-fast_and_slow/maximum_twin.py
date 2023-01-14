
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        
        slow_prev = None

        while fast and fast.next:
            fast = fast.next.next

            slow_next = slow.next
            slow.next = slow_prev
            slow_prev = slow
            slow = slow_next

        max_twin = 0
        while slow:
            max_twin = max(max_twin, slow_prev.val + slow.val)
            slow_prev = slow_prev.next
            slow = slow.next


        return max_twin
