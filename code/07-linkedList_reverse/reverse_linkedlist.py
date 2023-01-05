

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):

        prev = None
        curr = head

        while curr is not None:

            next_tmp = curr.next
            curr.next = prev

            prev = curr
            curr = next_tmp

        return prev



# === TESTING === #


# Create a linked list
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
head.next = node2
node2.next = node3

# Reverse the linked list
sol = Solution()
head = sol.reverseList(head)

# Print the reversed linked list
node = head
while node:
    print(node.val)
    node = node.next
