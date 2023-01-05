
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.results = []

        def depth_first_search(node, currentSum, targetSum):

            stack = [(node, [])]

            while stack:

                node, bt = stack.pop()
                bt = bt + [node.val]

                if node.left is None and node.right is None and sum(bt) == targetSum:
                    self.results.append(bt.copy())

                for child in [node.left, node.right]:
                    if child is not None:
                        stack.append((child, bt)) 

        if root is None: return []
        depth_first_search(root, 0, targetSum)
        return self.results
