
def reverse_linked_list(head, prev=None):
    # Base case: if the head is null, return the previous node
    if head is None:
        return prev

    # Save a reference to the next node
    next = head.next

    # Reverse the link between the head and the next nodes
    head.next = prev

    # Recursively call the function on the next node
    return reverse_linked_list(next, head)


# === TESTING === #

# Define a Node class
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Create a linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next = node2
node2.next = node3

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
node = head
while node:
    print(node.val)
    node = node.next
