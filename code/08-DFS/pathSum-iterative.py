# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def depth_first_search(node, currentSum, targetSum):

            stack = [(node, 0)]
            visited = set()

            while stack:

                node, curr = stack.pop()
                curr = curr + node.val

                if node in visited:
                    continue

                if node.left is None and node.right is None and curr == targetSum:
                    return True


                visited.add(node)

                for child in [node.left, node.right]:
                    if child is not None:
                        stack.append((child, curr))



        if root is None: return False
        return depth_first_search(root, 0, targetSum)
