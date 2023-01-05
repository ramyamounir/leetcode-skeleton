# problem 112: pathSum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def depth_first_search(node, currentSum, targetSum):

            # Base case: if the node is null, return
            if node is None:
                return

            # add sum and check
            currentSum += node.val
            if node.left is None and node.right is None and currentSum == targetSum: return True
            
            # Recursively call the function on the children of the node
            if depth_first_search(node.left, currentSum, targetSum) or  depth_first_search(node.right, currentSum, targetSum): return True

        
        if root is None: return False
        return depth_first_search(root, 0, targetSum)
